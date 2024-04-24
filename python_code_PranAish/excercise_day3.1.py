#1) Take values of length and breadth of a rectangle from user and check if it is square or not.

# len = int(input("Enter the value of length: "))
# bre = int(input("Enter the value of breadth: "))

# if(len==bre):
#     print("It is a square")
# else:
#     print("It is Rectangle")
    
    
#2) Take two int values from user and print greatest among them
3
# num1 = int(input("Enter Number1:"))
# num2 = int(input("Enter Number2:"))

# if(num1>num2):
#     print("The greatest number is",num1)
# else:
#     print("The greatest number is",num2)
    
    
'''3) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''


# item = int(input("Enter the number of items: "))
# quantity = item *100
# print(quantity)
# if(quantity>1000):
#     discount = quantity*10/100
#     total_cost = quantity - discount
#     print("total_cost")
#     print("Discount cost is: ",discount)
#     print("Cost: ",total_cost)
# else:
#     print("No Discount")
#     print("Cost: ",quantity)
    
    
    
'''4) A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade'''

#grade = int(input("Enter the marks of the students: "))

# if(grade<25):
#     print("F")
# if(grade>25 and grade<45):
#     print("E")
# if(grade>45 and grade<50):
#     print("D")
# if(grade>50 and grade<60):
#     print("C")
# if(grade>60 and grade<80):
#     print("B")
# else:
#     print("A")


# if(grade>25):
#     if(grade>25 and grade<45):
#         print("E")
#     elif(grade>45 and grade<50):
#         print("D")
#     elif(grade>50 and grade<60):
#         print("C")
#     elif(grade>60 and grade<80):
#         print("B")
#     else:
#         print("A")
# else:
#     print("F")

    
    #5) Take input of age of 3 people by user and determine oldest and youngest among them.
    
# age1 = int(input("Enter the age:"))
# age2 = int(input("Enter the age:"))
# age3 = int(input("Enter the age:"))

# if(age1>age2 and age1>age3):
#     print(f'{age1} is oldest')
# elif(age2>age1 and age2>age3):
#     print(f'{age2} is oldest')
# else:
#     print(f'{age3} is oldest')
    
# if(age1<age2 and age1<age3):
#     print(f'{age1} is youngest')
# elif(age2<age1 and age2<age3):
#     print(f'{age2} is youngest')
# else:
#     print(f'{age3} is youngest')
   

    
'''6) A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.'''

class_held = int(input("Number of classes held:"))
attend = int(input("Number of classes attended:"))
allowed = attend/class_held*100
print(allowed)
if(allowed>=75):
    print("student is allowed to sit in exam")
else:
    print("student is not allowed to sit in exam")
    