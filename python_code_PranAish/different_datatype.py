class my_exception(Exception): 
    pass

def create_heterogenous_list():

    lst = []
    num = int(input("Enter the number of elements: "))
    for i in range(num):
        ele = int(input("Enter integer elements: "))
        lst.append(ele)
    print(lst)

    num = int(input("Enter the number of elements: "))
    for i in range(num):
        ele = input("Enter charater elements: ")
        lst.append(ele)
    print(lst)

    lst1 = []
    num = int(input("Enter the number of elements: "))
    for i in range(num):
        ele = input("Enter the elements in list: ")
        lst1.append(ele)
    print(lst1)

    lst.append(lst1)
    print(lst)

    num = int(input("Enter the number of elements: "))
    for i in range(num):
        ele = float(input("Enter float elements: "))
        lst.append(ele)
    print(lst)


    lst_tup = []
    num = int(input("Enter the number of elements: "))
    for i in range(num):
        ele = input("Enter tuple elements: ")
        lst_tup.append(ele)
    # print(tuple(lst))
    same = tuple(lst_tup)
    lst.append(same)
    print(lst)

    dict_1 = {}
    num = int(input("Enter the number of elements: "))
    print("Enter the element in dictonary: ")
    for i in range(num):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict_1[key] = value
    print(dict_1)
    lst.append(dict_1)
    print(lst)

    set_1 = set()
    num = int(input("Enter the number of elements: "))
    for i in range(num):
        ele = int(input("Enter the elements in set: "))
        set_1.add(ele)
    lst.append(set_1)
    print(lst)
    
      
    is_homogeneous = True
    j = lst[0]

    for i in range(1,len(lst)):
        if(type(j)!= type(lst[i])):
            is_homogeneous = False
            break
    if is_homogeneous:
        raise my_exception
    else:
        print("We return a hetrogeneus list")

create_heterogenous_list()