from design_patterns.singleton.antipattern.my_singleton import MySingleton

if __name__ == '__main__':

    s1 = MySingleton()
    s2 = MySingleton()
    print(type(s1))
    print(type(s2))