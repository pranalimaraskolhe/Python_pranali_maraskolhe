
"""
2) Create a program named "my_dict_store" which support following operations on 
dictionary named "capitals" which would have keys as their country and values as their capitals
respectively from the user
for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
is provided by the user 

"""

# Sample code template for my_dict_store
def dict_display_capitals(capitals): 
       print(capitals) 
     
def dict_add_element(capitals):
    print("Before adding a key and value ",capitals)
    key = input('Please enter the key ')    
    value = input('Please enter the value ')    
    capitals[key] = value
    print(capitals) 
        
def dict_add_elements(capitals):
    print("Before adding a dict ",capitals)
    no_of_items = int(input("How many items you want to add "))
    for i in range(0,no_of_items,1):
        key = input('Please enter the key ')    
        value = input('Please enter the value ')    
        capitals[key] = value
    print(capitals) 
        
def dict_remove_element(capitals):
    print("before",capitals)
    del capitals[input()]
    print(capitals)

def dict_show_value_for_a_key(capitals):
    print(capitals)
    print(capitals[input()])
    
def dict_update_or_add_a_key(capitals):
    print("Before Update",capitals)
    k=input("Enter the key ")
    capitals.update({k:input("Update new value ")})
    print("After update",capitals) 

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
	
    capitals= {}
    """
        # Write your code here to create the dictionary from the user and reference it with capitals
        """
    no_of_items = int(input("How many items you want to add "))
    for i in range(0,no_of_items,1):
        key = input('Please enter the key ')    
        value = input('Please enter the value ')    
        capitals[key] = value 
    
    # d.update({key:value})) 
    #keys = input("Please enter the countries as keys for ex : India,USA,Srilanka").split(',')
    #for elem in keys :
    #    capitals[elem] = input(f"Please enter the capital for {elem}: ").strip()
    
    print(capitals)
    
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Show Values for a key")
        print("    6: Update value of a key")
        print("    7: Exit")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            dict_show_value_for_a_key(capitals)
        elif choice ==6:
            dict_update_or_add_a_key(capitals)
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()