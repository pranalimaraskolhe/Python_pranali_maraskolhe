# ------------------------------------------------
# Exercise : Exceptions
# -------------------------------------------------

# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

# def color():
#     dict={'1':'red','2':'blue','3':'orange'}
#     key= input("Enter the key: ")
#     print(dict[key])
# try:
#     color()
# except:
#      print("Color does not exists:")
    
# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 

# def ele():
#     lst=[]
#     ele1=int(input("Enter the number of elements: "))
#     for i in range(ele1):
#         var=input("Enter the elements: ")
#         lst.append(var)
#     print(lst)
#     key=int(input("Enter the index: "))
#     print(lst[key])
# try:
#     ele()
# except IndexError:
#     print("Value not found if the index does not exists ")
# finally:
#     print("Program has been executed successfully")
    
# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)


# class my_exception(Exception):
#     pass

# def age():
#     age=int(input("Enter the age of a person: "))
#     total_no_days= age*365
#     print(total_no_days)
    
#     if (total_no_days>100001):
#         print("you lived for so long , may be you will die soon:")
#         raise my_exception
    
# age()
    

# 4)Create the following program named "my_exception_store" with the menu below :

print("Welcome User , What would you like to do today ?")
   # 1) Create a postive numbered list 
   # Note : raise an exception if the users inserts a negative number OR user creates an empty list 
   
# class my_exception(Exception): 
#     pass
 
# def create_positive_numbered_list():
#     my_int_list1=[]
#     num = int(input("Enter numbers: "))
#     if num > 0:
#         my_int_list1.append(num)
#     else:
#         raise my_exception
#     print(my_int_list1)
    
        
# create_positive_numbered_list()
   
#     2) Create a negative  numbered list 
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
# class my_exception(Exception): 
#     pass
 
# def create_negative_numbered_list():
#     my_int_list1=[]
#     num = int(input("Enter numbers: "))
#     if num < 0:
#         my_int_list1.append(num)
#     else:
#         raise my_exception
#     print(my_int_list1)
    
# create_negative_numbered_list()



#     3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
class my_exception(Exception): 
    pass
def create_heterogenous_list():
    my_het_list3 = []
    ele = int(input("Enter size of list"))
    for i in range(ele):
        num = input("Enter the data: ")
        my_het_list3.append(num)
       
    print(my_het_list3)
    
    # same = my_het_list3[0]
    print(type(my_het_list3[0]))
    # for i in my_het_list3:
    #     
    
    
create_heterogenous_list()

#     4) Refresh the program to start with blank lists
#     5) Exit

# Handle exceptions in the script for all operations 
# and let the user continue till he chooses to exit from the program 

# # reference code :

# def my_exception_store(): 
#     my_int_list1=[]
#     my_int_list2=[]
#     my_het_list3=[]

#     while(True):
#         try:
#             print("Welcome to my_exception_store !!!!")
#             print("-------------------------------------")
#             print("Following operations are supported :")
#             print("1) Create a positive numbered list  ")
#             print("2) Create a negative numbered list  ")
#             print("3) Create a heterogenous list ")
#             print("4) Refresh the program to start with blank lists")
#             print("5) Exit  ")
            
#             choice = int(input("Please enter your choice !!!! "))
#             if choice ==1:
#                 create_positive_numbered_list(my_int_list1)
#             elif choice ==2:
#                 create_negative_numbered_list(my_int_list2)
#             elif choice ==3:
#                 create_heterogenous_list(my_het_list3)
#             elif choice ==4:
#                 my_int_list1.clear()
#                 my_int_list2.clear()
#                 my_het_list3.clear()
#                 print("Store restarted !!!! ")
#             elif choice ==5:
#                 break
#             else:
#                 print("Please choose something from the above")
#         except negative_number_error:     
#             print("We received a negative number in the list and I handled negative_number_error exception")
#             my_int_list1.clear()
#         except positive_number_error:     
#             print("We received a positive number in the list and I handled positive_number_error exception")
#             my_int_list2.clear()
#         except homogenous_list_error:    
#             print("We received a Homogenous list and I handled homogenous_list_error exception")
#             my_het_list3.clear()
            
# my_exception_store()   