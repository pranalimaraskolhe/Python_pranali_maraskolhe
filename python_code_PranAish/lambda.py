# def addition(first_num, second_num):
#     return first_num+second_num

# def multiplication(first_num, second_num):
#     return first_num*second_num


addition_lambda = lambda first_num, second_num : first_num+second_num
multiplication_lambda = lambda first_num, second_num : first_num*second_num

# print(addition(1,2))
# print(addition_lambda(1,2))

# # print(multiplication(1,2))
# print(multiplication_lambda(1,2))


# # ------------------------- our function my_calculator
# def my_calculator():
    
#     print("1: Addition \n 2: Multiplication")
#     choice = int(input("Please enter choice"))
    
#     num1= int(input("Number1:"))
#     num2= int(input("Number2:"))

#     if choice ==1 :
#         print("addition:",addition(num1,num2))
#     else:
#         print("multiplication",multiplication(num1,num2))

# my_calculator()        

   
def my_calculator_lamdba():
    print("1: Addition \n 2: Multiplication")
    choice = int(input("Please enter choice"))
    
    num1= int(input("Number1:"))
    num2= int(input("Number2:"))

    if choice ==1 :
        print("addition:",addition_lambda(num1,num2))
    else:
        print("multiplication",multiplication_lambda(num1,num2))

my_calculator_lamdba()       


# exploring function with multiple arguments 
def addition_nargs(*args):
    sum=0
    for val in args:
        sum += val
    return sum

print(addition_nargs(1,2,3,4))

def addition_nkeyword_args(**kwargs):
    sum=0
    for val in kwargs.values():
        sum += val
    return sum

print(addition_nkeyword_args(first_num = 1,second_num= 2,third_num= 3))    