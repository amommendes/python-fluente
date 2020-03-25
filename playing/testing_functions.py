def myFunc(class_,sub_dag_name,accounts):
    return ("Na factory: {},{},{}".format(class_,sub_dag_name,accounts))

def clean_sub_dag(sub_dag_name, class_, accounts):
    sub_dag = myFunc(
        class_=class_,
        sub_dag_name=sub_dag_name,
        accounts=accounts,
    )
    print(sub_dag)
    return sub_dag

def get_sub_dag_operator(dag,sub_dag_name,sub_dag_func,**kwargs):
        print(kwargs)
        return sub_dag_func(sub_dag_name, **kwargs)


if __name__ == "__main__":
    google_ads_clean_dag = get_sub_dag_operator(
        dag="main_dag",
        sub_dag_func=clean_sub_dag,
        sub_dag_name='google-ads-raw-to-clean',
        class_="ads",
        accounts=["class_",2]
    )

