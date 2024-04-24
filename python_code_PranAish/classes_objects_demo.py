
class Employee:
  # class variable 
  cls_department_name= "CDAC"
  
  def __init__(self,rcv_empid,rcv_emp_salary,rcv_mgr_id):
    # instance variables 
    self.emp_id= rcv_empid
    self.emp_salary= rcv_emp_salary
    self.mgr_id= rcv_mgr_id
    print(f"{self} was created successfully with values {rcv_empid},{rcv_emp_salary},{rcv_mgr_id}")

  # instance method
  def get_emp_salary(self):
      return self.emp_salary
  
  # instance method
  def set_emp_salary(self,rcv_salary):
      self.emp_salary = rcv_salary

  # class method 
  @classmethod
  def get_department_name(cls):
      return cls.cls_department_name
  
  # static method
  @staticmethod
  def field_expertise():
      print("Some expertise printed here")
  
def main():

    # 1) create an object employee(100,1000,1)  
    my_first_emp_obj = Employee(100,1000,1)
    
    #2) do the following for the created object
    #direct access using .notation
    print(f"Employee id for the object is {my_first_emp_obj.emp_id}")
    print("employee_1.get_emp_salary():",my_first_emp_obj.get_emp_salary())
    print(f"Manager id for the object is {my_first_emp_obj.mgr_id}")
    
    #3) print the department name 
    Employee.get_department_name()
    my_first_emp_obj.get_department_name()
    
    #4) display the expertise for the employees
    Employee.field_expertise()
    my_first_emp_obj.field_expertise()
  
    # 5) Deleting Attributes and Objects
    
    del my_first_emp_obj.emp_id
    try:
        print(my_first_emp_obj.emp_id)
    except Exception:
        print("We did not find empid in employee1 object post deletion")    

    del my_first_emp_obj
    try:
        print(my_first_emp_obj)
    except Exception:
        print("We did not find employee1 object post deletion") 
main()   


class My_airline :
    airline_name = 'Gaurav Airline'
    cities = {'Delhi','Pune','Mumbai','Bangalore','Chennai','Hyderabad','Patna','Trivandrum'}
    rows = set(range(1,21))
    section = {'A','B','C','D','E','F'}
    flight_numbers = set(range(564262,564270))
    
    def __init__(self,rcv_dep = None , rcv_arr= None):
        
        if rcv_dep is None: 
            self.departure =  My_airline.cities.pop()
        else: 
            self.departure =  rcv_dep
            
        if rcv_arr is None:
            self.arrival = My_airline.cities.pop()  
        else:
            self.arrival =rcv_arr
            
        self.flight_number =  My_airline.flight_numbers.pop()  
        self.seat_number = str(My_airline.rows.pop()) + My_airline.section.pop() 
        
    def display_details(self):
        print(f"""Your ticket details :
--------------------------------------               
Airline_name : {My_airline.airline_name}
Flight_number : {self.flight_number}
Departure: {self.departure}
Arrival: {self.arrival}
Seat_number: {self.seat_number}
              
              """)   


def main():
   ticket_number1 = My_airline('LONDON','USA') 
   ticket_number2 = My_airline()
   ticket_number3 = My_airline(input("departure"),input("arrival")) 
   
   ticket_number1.display_details()
   ticket_number2.display_details()
   ticket_number3.display_details()

main()

































# # Initial explaination for class and object creation

# class Student:
#     # class variable
#     school_name = "CDAC"    

#     # initialiser
#     def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
#         # instance variable
#         self.student_name = rcv_name      # public instance variable 
#         self.student_rollno = rcv_rollno   # public instance variable 
#         self.student_pocket_money = rcv_pocket_money # public instance variable 
#         self.student_enrolled_coursename = rcv_course # public instance variable 
#         self.__student_bank_balance = set([298738,902803,72637,5625,565]).pop()
#         print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course}")

#     # instance method
#     def get_enrolled_course(self):
#         return self.student_enrolled_coursename

#     # instance method
#     def get_student_pocket_money(self):
#         return self.student_pocket_money
    
#     # instance method
#     def enroll(self,rcv_course_name):
#         self.student_enrolled_coursename = rcv_course_name

#     # instance method
#     def unenroll(self):
#         self.student_enrolled_coursename = None
        
#     # instance method
#     def get_student_bank_balance(self):
#         return self.__student_bank_balance

#     # class method
#     @classmethod
#     def change_schoolname(cls,rcv_schoolname):
#         cls.school_name = rcv_schoolname
    
#     # static method
#     @staticmethod
#     def display_facilities_available():
#         print("Facilities are 1) Gym ---- 2)Library ---- 3)TT\n")
    
#     # Operator Overloading -- implemented this to support greater than operation for Student class 
#     def __gt__(self,other_obj):
#         return self.student_rollno > other_obj.student_rollno       

#     # Operator Overloading -- implemented this to support Equal to operation for Student class 
#     def __eq__(self,other_obj):
#        return (self.student_name == other_obj.student_name  and 
#                self.student_rollno == other_obj.student_rollno and
#                self.student_pocket_money == other_obj.student_pocket_money and
#                self.student_enrolled_coursename == other_obj.student_enrolled_coursename)
			
#     def __del__(self):
#     # body of destructor   
#         print("I am in destructor ")

# # main method which is outside the class 
# def main():
#     print("I am in main and I am not part of the class ")

#     # create a Student object referenced by gaurav
#     gaurav= Student("Gaurav",1,100,'Python')
#     duplicate_gaurav= Student("Gaurav",1,100,'Scala')
    
#     # # access the public instance variable for gaurav referenced object directly 
#     # print("Before setting the public variable : ",gaurav.student_pocket_money) 
#     # # set the public variable outside the class 
#     # gaurav.student_pocket_money = 9999999
#     # print("After setting the public variable : ", gaurav.student_pocket_money) 
    
#     # # invoke a instance method(getter) for gaurav referenced object to access an attribute of the class 
#     # print(gaurav.get_student_pocket_money())
    
#     # print("Before Unenroll call ", gaurav.get_enrolled_course())
#     # # invoke a instance method(setter) for gaurav referenced object to set an attribute of the class 
#     # gaurav.unenroll()
#     # print("After Unenroll call ", gaurav.get_enrolled_course())
#     # # invoke a instance method for gaurav referenced object 
#     # gaurav.enroll("Scala")
#     # print("After Enroll call ", gaurav.get_enrolled_course())

#     # # create another Student object referenced by pratik
#     pratik= Student("Pratik",2,200,'Java')
 
#     # # trying to change the class variable using the Class reference 
#     # # print the class variable using each of the available references 
#     # print("School name at Class level was",Student.school_name)
#     # print("Gaurav School name was",gaurav.school_name)
#     # print("Pratik School name was",pratik.school_name)
    
#     # # invoke class method(setter) using Student class reference
#     # Student.change_schoolname("Sunbeam")

#     # # print the class variable 
#     # print("School name at Class level is",Student.school_name)
#     # print("Gaurav School name is",gaurav.school_name)
#     # print("Pratik School name is",pratik.school_name)

#     # # trying to change the class variable using the instance reference gaurav but via a class method
#     # # print the class variable using each of the available references 
#     # print("School name at Class level was",Student.school_name)
#     # print("Gaurav School name was",gaurav.school_name)
#     # print("Pratik School name was",pratik.school_name)

#     # # invoke class method(setter) using gaurav instance variable reference
#     # gaurav.change_schoolname("Sunbeam1")

#     # # print the class variable 
#     # print("School name at Class level is",Student.school_name)
#     # print("Gaurav School name is",gaurav.school_name)
#     # print("Pratik School name is",pratik.school_name)

#     # # invoke the static method 
#     # Student.display_facilities_available()
#     # gaurav.display_facilities_available()
#     # pratik.display_facilities_available()
#     # #display_facilities_available() # doesnot work 
    
    
#     # try:
#     #     print("gaurav bank balance is ", gaurav.__student_bank_balance)
#     # except:
#     #     print("Private variable accessed -- exception occured")
     
#     # print("gaurav bank balance is ", gaurav.get_student_bank_balance())
    
#     # # create a Student object referenced by gaurav_copy
#     # gaurav_copy= Student("Gaurav",1,100,'Python')
    
#     # if gaurav < pratik:
#     #     print(f"Gaurav rollno: {gaurav.student_rollno} is greater than that of Pratik  rollno: {pratik.student_rollno}")
#     # else:
#     #     print(f"Pratik rollno: {pratik.student_rollno} is greater than that of Gaurav rollno: {gaurav.student_rollno}")    

#     # if gaurav == gaurav_copy:
#     #     print("both objects have same contents ")
#     # else:
#     #     print("both objects DO NOT have same contents ")    
    
#     # # Deleting Attributes student_pocket_money
#     # print(gaurav.student_pocket_money)
    
#     # # AttributeError: 'Student' object has no attribute 'student_pocket_money'
#     # del gaurav.student_pocket_money 
#     # # print(gaurav.student_pocket_money)
#     # print(pratik.student_pocket_money)
    
    
#     # miscellnous functions for the class 
#     # list all that the Student Class contains 
#     print(dir(Student))
#     print(Student.__doc__)
    
#     # destructor
    
#     # two references to the same object and deleting any one of the reference 
#     gaurav_duplicate_reference = gaurav
#     del gaurav_duplicate_reference
#     print(gaurav.get_enrolled_course())
#     # print(gaurav_duplicate_reference.get_enrolled_course())
    
#     """  Deleting entire object gaurav
#     The destructor was called after the program ended or when all the references to object are #deleted i.e when the reference count becomes zero, not when object went out of scope.
#     """
#     # UnboundLocalError: local variable 'gaurav' referenced before assignment
#     del gaurav
#     print(gaurav.get_enrolled_course())
    
# # invoke the main function 
# main()






