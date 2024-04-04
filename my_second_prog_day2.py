print("I am in second module")

#import my_second_program as f # importing the entire module 
from my_second_program import my_name,my_list  # import part of modules 
 
print("second module output :> my_name in first module is ===>>>>>> " , my_name)
print("second module output :> my_list in first module is ===>>>>>> " , my_list)
