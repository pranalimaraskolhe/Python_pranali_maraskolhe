'''1) Accept two numbers from the user and print 
a) addition 
b) first number squared 2 
c) first number raised to second number '''

def add_fun(num1,num2=2):
    print("Addition is: ",num1 + num2)
    print("Square of number1:", num1*num1)
    print("first number raised to second",num1**num2)
   
    
#2) Accept String from user and output upper case of the input string 

def str_upper(str='aa'):
    str = input("Enter your Name: ")
    upper_string = (str.upper())
    return upper_string



# '''3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console'''

def salary(raise_salary_percentage=12):
    name = "Pranali"
    existing_salary = 900 
    raise_salary_percentage = int(input("Enter the raise salary percentage: "))

    hike = raise_salary_percentage/100

    raise_salary = existing_salary * hike + existing_salary

    return raise_salary


#4) Get the height from the user in cms and display the user height back to console in foot/feet and inches

def height(height=1):
   # height=int(input("Enter your height: "))

    height_in_feet=height/30.48

    print(f'In Feet: {round(height_in_feet,2)}')

    height_in_inch= height_in_feet * 12

    print(f'In Inch: {round(height_in_inch,2)}')
    
    
    
#5) Get the no of the dollars from the user apply the conversion of 1 dollar = 82 rupees and print the amount to the console in rupees

def dollar(dollar=5):
    dollar = int(input("Enter the dollar: "))

    current_dollar = dollar * 82

    print(f'${dollar} is: Rs.{current_dollar}')
    
    '''6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
       string ex: "fare from mumbai to pune is 400 INR with has a discount of 5%" '''
    
    
def travel(source,destination,fare,discount=5):
    source = input("Enter your source: ")
    destination = input("Enter your destination: ")
    fare = int(input("Enter fare: "))
   # discount = int(input("Enter discount: "))
    after_discount = fare - fare * discount/100
    print(f'fare {source} to {destination} is {fare} INR with has a discount of {discount}% it is {after_discount} INR')
