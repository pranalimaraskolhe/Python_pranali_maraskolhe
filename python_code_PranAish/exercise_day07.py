# -------------------------------------------
# Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_salary
#    mgr_id
#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:
# main

# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects

# department_name = "IT"

# class Employee:
#     def __init__(self,empid,emp_salary,mgr_id):
#         self.employee_id = empid
#         self.employee_salary = emp_salary
#         self.manager_id = mgr_id
    
    
#     def get_emp_id(self):
#         return self.employee_id
    
#     def get_emp_salary(self):
#         return self.employee_salary
    
#     def get_manager_id(self):
#         return self.manager_id
    
    
#     def set_emp_salary(self,rcv_salary):
#         self.employee_salary = rcv_salary
        
        
#     @classmethod
#     def get_department_name(self):
#         return self.department_name
    
#     @staticmethod
#     def field_expertise():
#         print("1.web development 2. Python 3. Java") 
        
        
# def main():
#     Aishwarya = Employee(100,1000,1)  
#     print("Employee id of aishwarya is",Aishwarya.employee_id)
#     print("Salary of aishwarya is",Aishwarya.employee_salary)
#     print("Manager id of aishwarya is",Aishwarya.manager_id)
    
#     print("department name",department_name)
    
#     Aishwarya.field_expertise()
    
#     try:
#         del Aishwarya
#         print(Aishwarya.employee_id)
        
#     except:
#         print("Object does not exist")
        
    
    
# main()

# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 

import random



class AirLine_Tickets:
    
    airline_name = "Indigo"
    
    def __init__(self,depature,arrival_cities,flight_num,seat_assign):
        self.flight_depature = depature
        self.flight_arrival_cities = arrival_cities
        self.flight_flight_number = flight_num
        self.flight_seat = seat_assign
        
    def get_depature(self):
        return self.flight_depature
    
    def get_flight_arrival_cities(self):
        return self.flight_arrival_cities
    
    def set_flight_number(self,flight_num):
        self.flight_flight_number = flight_num.random()
    
    def get_flight_seat(self,seat_assign):
        self.flight_seat = seat_assign(['A','B','C','D','E','F']).random()
    
    @classmethod
    def change_airline_name(cls,rcv_airline_name):
        cls.airline_name = rcv_airline_name
        
    # @staticmethod
    
    # def display():
    #     print("Flights Details:")
    #     print(f'Airline Name: {AirLine_Tickets.airline_name}')
        
def main():
    
    Aishwarya = AirLine_Tickets(depature)
    
    
   
    
    
    
    main()