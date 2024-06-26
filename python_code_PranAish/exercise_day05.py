"""
3)  Create a program named "my_set_store" which support following operations on two sets
    provided by user 

for ex: 
	A = {1,2,3,4,5}
	B = {18,19,20,21}
is provided by the user

Operations supported by our program are :
	1: Union
	2: Intersection 
	3: A-B
	4: B-A
	5: Take a element from user and Display if that element is a member of set B 
	6: Display number of elements in the set A
    7: Display number of elements in the set B
	8: Add an element taken from the user to the set A
	9: Add multiple elements taken from the user to the set A
	10: Remove an element taken from the user from set A
"""

# Sample code template for my set store
def set_union(setA,setB) :
	print("union",setA.union(setB))
      

def set_intersection(setA,setB) :
	print("Intersection",setA.intersection(setB)) 

def set_minus(setA,setB) :
	print("difference",setA.difference(setB)) 

def is_member_of_set(setB) :
    
    # blank_set = set()
    # for i in range(int(input("element count"))):
    #     blank_set.add(int(input("element")))
    # print(blank_set)
    # num = int(input("Enter number"))
    # print(num in blank_set)
    
    setC = set()
    for i in setB:
        print(setC.add(int(i)))
    print(setC)
    num = int(input("Enter number"))
    print(num in setC)
    print(setB)
    print(setC)
  

def set_display(setA):
	print("elements in setA:",len(setA)) 
		
def set_add_element(setA):
    print(setA)
    num = int(input("Enter the number: "))
    print("Add Elemnet: ",setA.add(num))
    print(setA)
    

def set_add_elements(setA):
    num = set(input("Enter number: ").split(","))
    print(setA.update(num))
    print(setA)
    

def set_remove_element(setA):
    print(setA)
    blank_set = set()
    for i in range(int(input("element count"))):
        blank_set.add(int(input("element")))
    print(blank_set)
    num = int(input("Enter number: "))
    print(blank_set.remove(num))
    print(blank_set)

def my_set_store():
	print("\n Welcome to Our Set Store !!! ")

	setA= set(input("Please enter comma seperated elements for the set A").split(","))
	setB= set(input("Please enter comma seperated elements for the set B").split(","))
 
	while(True):
		print("\n*************** Menu **********************")
		print("Operations supported by our program are :")
		print("	1: Union")
		print("	2: Intersection ")
		print("	3: A-B")
		print("	4: B-A")
		print("	5: Take a element from user and Display if that element is a member of set B ")
		print("	6: Display number of elements in the set A")
		print(" 7: Display number of elements in the set B")
		print("	8: Add an element taken from the user to the set A")
		print("	9: Add multiple elements taken from the user to the set A")
		print("	10: Remove an element taken from the user from set A")
		print(" 11: Exit")

		choice = int(input("Please enter your choice "))

		if choice   ==1:
			set_union(setA,setB) 
		elif choice ==2:
			set_intersection(setA,setB)
		elif choice ==3:
			set_minus(setA,setB)
		elif choice ==4:
			set_minus(setB,setA)
		elif choice ==5:
			is_member_of_set(setB) 
		elif choice ==6:
			set_display(setA)
		elif choice ==7:
			set_display(setB)
		elif choice ==8:
			set_add_element(setA)
		elif choice ==9:
			set_add_elements(setA)
		elif choice ==10:
			set_remove_element(setA)
		elif choice ==11:
			break
		else:
			print("Invalid Input , Please Try Again !!!!  ")  
			
my_set_store()	