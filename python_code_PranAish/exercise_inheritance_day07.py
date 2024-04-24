'''-------------------------
Exercise on Inheritance:
-------------------------
1. Create a base class named Employee as follows:
Employee (
-- class variables and methods
	organisation_name, 
	get_organisation_name(),
	set_organisation_name(org_name)

-- instance variables and methods()
emp_id,
name,
base_location,
deployed_location,
designation,
salary ,
get_employee_details() 	



Create a subclass of Employee named Manager as follows:
Manager(
	
	-- instance variables and methods()
	managed_employees[], # this is list of emp_references
	perform_appraisal_for_an_employee(emp_reference,percent_raise),
	get_manager_details()
)

Write a main method that does the following:
create 3 objects of Employee 
create an object of Manager_class and add the above 3 employee objects created as managed employees 
display get_manager_details()
for an employee do perform_appraisal_for_an_employee()'''



class Employee:
    
    organisation_name = "CDAC"
    
    def __init__(self,emp_id,name,base_location,deployed_location,designation,salary):
        self.emp_num = emp_id
        self.emp_name = name
        self.location = base_location
        self.deployed = deployed_location
        self.emp_designation = designation
        self.emp_salary = salary
        
    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name
    
    def set_organisation_name(cls,org_name):
        cls.organisation_name = org_name
        
    def get_emp_id(self):
       return self.emp_num
   
    def get_name(self):
        return self.emp_name
    
    def get_location(self):
        return self.location
    
    def get_base_location(self):
        return self.deployed
    
    def get_designation(self):
        return self.emp_designation
    
    def get_salary(self):
        return self.emp_salary
    
    
def main():
    
    ash = Employee(1,'Ash','Pune','Mumbai','SE',30000)
    
    print(ash.emp_num)
    print(ash.emp_name)
    print(ash.location)
    print(ash.deployed)
    print(ash.emp_designation)
    print(ash.emp_salary)
    
    
main()
        
    

# '''----- Inheritance exercise ----
# 2. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes '''


