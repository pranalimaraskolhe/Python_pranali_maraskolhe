from  function_definitions import *
# import function_definitions

# first_num = int(input("Please enter First number:"))
# second_num = int(input("Please enter Second number:"))
# returned_value = my_addition(first_num,second_num)
# print("The Addition of the numbers is ",returned_value)

# returned_value = my_square(first_num)
# print("The Square of the number is ",returned_value)

# returned_value = my_exponenation(first_num,second_num)
# print("The exponenation of the numbers is ",returned_value)

# my_string = input("Please enter a String: ")
# returned_value = my_uppercase_func(my_string)
# print("Upper case of the string is ",returned_value)

# existing_salary = int(input("Pleased enter the existing_salary"))
# raise_salary_percentage = int(input("Pleased enter the percentage"))

# returned_value= raise_sal_percent(existing_salary,raise_salary_percentage)
# print("The incremented salary is ",returned_value)

# height = int(input("Pleased enter height in cms "))
# returned_value= get_height(height)
# print("Height in feet is ",returned_value)

# no_of_dollars = int(input("Pleased enter no of dollars "))
# returned_value= convert_to_rupee(no_of_dollars)
# print("Amount is INR is " ,returned_value)

source = input("Pleased enter the source ")
destination = input("Pleased enter the destination ")

fare = float(input("Pleased enter the fare "))
discount_rate = float(input("Pleased enter the discount_rate in percentage "))

returned_value=get_fare_details(source, destination, fare, discount_rate)
print(returned_value)

# alternative solutions
def get_fare_details1(fare_in_INR, discount_rate_percentage):
    """
    6) receive source, destination, fare in INR, discount_rate percentage from the user and return the 
    string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"
    """
    return  fare_in_INR- (fare_in_INR*discount_rate_percentage/100)

source= "Pune"
destination = "Mumbai"
fare= 400
discount= 5
return_val = get_fare_details1(fare,discount)
print(f"Fare from {source} to {destination} is {fare} INR after applied discount of {discount}% it is {return_val}")

# alternative solutions
def get_fare_details2(fare_in_INR, discount_rate_percentage):
    """
    6) receive source, destination, fare in INR, discount_rate percentage from the user and return the 
    string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"
    """
    return  (source, destination, fare_in_INR, discount_rate_percentage,fare_in_INR- (fare_in_INR*discount_rate_percentage/100))

source= "Pune"
destination = "Mumbai"
fare= 400
discount= 5
return_val = get_fare_details2(fare,discount)
print(f"Fare from {return_val[0]} to {return_val[1]} is {return_val[2]} INR after applied discount of {return_val[3]}% it is {return_val[4]}")