#Factorial
def factorial(num=5):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    
    return fact

print(factorial(5))
    

# create a function that  take a number from the user and returns a list of  even numbers from 1 to that number 

def even(num=1):
    num = int(input("Enter number: "))
    lst = []
    for i in range(0,num,2):
       lst.append(i)
    return lst

          
print(f'Even number is : {even()}')
    
    
#Addition of even number:

def even(num=1):
    num = int(input("Enter number: "))
    sum = 0
    # lst = []
    for i in range(0,num,2):
       sum = sum + i
    return sum

          
print(f'Addition of Even number is : {even()}')
    
# create a fun10
# ction that takes in a number from the user and returns a tuple of all Odd numbers from 1 to that number 

def odd(num=1):
    
    lst = []
    for i in range (1,num,2):
      lst.append(i)
    print(f'Odd Number :{tuple(lst)}')
   
    
   
odd(10)



# create a function that takes in temperature in Celsius and returns temperature in Farenhiet

def temp(C):
    f = (C * 9/5) + 32
    return f

print(temp(round(100)))
