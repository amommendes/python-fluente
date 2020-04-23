import os
from collections import namedtuple
import re
import csv
from pathlib import Path

def _is_file(path_dir, child):
    return os.path.isfile(os.path.join(path_dir, child)) and (child != "__init__.py") and (child.split(".")[1] == "py")


def _is_directory(path_dir, directory):
    return directory != "__pycache__" and os.path.isdir(os.path.join(path_dir, directory)) is True

dag_attributes = namedtuple("DagAttr", "file_path,catchup,start_date")


def get_file_attributes(file_path: str, record: namedtuple,
                        patterns: list = [".*catchup.*", "MAIN_START_DATE = datetime\((\d{4},\s\d+,\s\d+).*"]):
    records = []
    catchup_pattern = re.compile(patterns[0])
    start_date_pattern = re.compile(patterns[1])
    with open(file_path, 'r') as f:
        content = f.readlines()
        catchup = "".join([re.sub("[\n\s,]", "", line) for line in content if catchup_pattern.match(line)])
        start_date = "".join(
            [re.sub("MAIN_START_DATE = datetime\((\d{4},\s\d+,\s\d+).*\n", "\\1", line) for line in content if
             start_date_pattern.match(line)])
        records.append(record(file_path=file_path, catchup=catchup, start_date=start_date))
    return records


if __name__ == "__main__":
    path = os.path.join(
        os.getenv("HOME"),
        "abraca-data/bi-etl-ejuice/bietlejuice/jobs/composer/dags")
    directories = (os.path.join(path, directory) for directory in os.listdir(path)
                   if _is_directory(path, directory) )

    dag_files = [{"file_path": directory + "/" + child, "record": dag_attributes}
                 for directory in directories for child in os.listdir(directory)
                 if _is_file(directory, child)
                 ]
    records = map(lambda dag_file: get_file_attributes(**dag_file), dag_files)

    with open("./data.csv", 'w') as f:
        writer = csv.writer(f)
        for record in records:
            record = record[0]
            row = [record.file_path, record.catchup, record.start_date]
            writer.writerow(row)
