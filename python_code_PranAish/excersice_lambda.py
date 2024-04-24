

# add = lambda num1,num2: num1+num2
# square = lambda num1 : num1*num1
# power_fun = lambda num1, num2 : num1**num2

# def calculator():
#     # print("1. Addition\n2.Square\n3.Power")
#     # ch = int(input("Enter choice: "))
#     ans = 'y'
    
#     while(ans!='y' or ans!='Y'):
#         print("1. Addition\n2.Square\n3.Power")
#         ch = int(input("Enter choice: "))
    
#         if ch == 1:
#             num1= int(input("Number1:"))
#             num2= int(input("Number2:"))
#             print(f'Addition is {add(num1,num2)}')
            
#         elif ch == 2:
#             num1 = int(input("Number1: "))
#             print(f'Sqaure is {square(num1)}')  
            
#         elif ch == 3:
#             num1= int(input("Number1:"))
#             num2= int(input("Number2:"))
#             print(f'First number raised to second number is {power_fun(num1,num2)}')
        
#         else:
#             print("Invalid input")
#             print("Enter your valid choice: ")
#             print("\n")
        
        
        
#     ans = input("Do you want to continue press (Y/N): ")
    
# calculator()


# 2) Accept String from user and output upper case of the input string 

# string_upper = lambda str1 : str1.upper()

# def convert_string():
#     str1 = input("Enter string: ") 
#     print(f"Converted Upper case string is: {string_upper(str1)}")
    
# convert_string()


# '''3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console'''

raise_salary = lambda raise_salary_percentage : 900 * raise_salary_percentage/100 + 900

def salary_raise():
    Name ='Pranali'
    existing_salary = 900 
    
    raise_salary_percentage = float(input("Enter the raise salary percentage: "))
    
    print(f'Raised Salary of {Name} form {existing_salary} with {raise_salary_percentage} is {raise_salary(raise_salary_percentage)}')
    
salary_raise()


# 4) Get the height from the user in cms and display the user height back to console
#    in foot/feet and inches eg : 155 in cms displays 5.09 in feet and inches

# height_in_feet = lambda height :  height/30.48

# height_in_inch = lambda height_in_feet : height_in_feet * 12

# def height():
    
#     height = int(input("Enter your height: "))
    
#     print(f'height_in_feet: {round(height_in_feet(height))}')
#     print(f'height_in_inch: {round(height_in_inch(height))}')
    
# height()

#5) Get the no of the dollars from the user apply the conversion of 1 dollar = 82 rupees and print the amount to the console in rupees

# current_dollar = lambda dollar : dollar * 82

# def dollar_rupee():
#     dollar = int(input("Enter the dollar: "))
#     print(f'${dollar} is: Rs.{current_dollar(dollar)}')
    
# dollar_rupee()

# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"

# travel = lambda fare, discount : fare - fare * discount/100

# def tour():
#     source = input("Enter your source: ")
#     destination = input("Enter your destination: ")
#     fare = int(input("Enter fare: "))
#     discount = int(input("Enter discount: "))
    
#     print(f'fare {source} to {destination} is {fare} INR with has a discount of {discount}% it is {travel(fare,discount)} INR')
    
# tour()

