from design_patterns.singleton.antipattern.my_singleton import MySingleton

if __name__ == '__main__':

    s1 = MySingleton()
    s2 = MySingleton()
    MySingleton._instance = None
    s3 = MySingleton()

    print(type(s1))
    print(type(s2))
    print(type(s3))
