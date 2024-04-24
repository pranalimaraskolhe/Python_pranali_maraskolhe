## 1: write a program to take some text lines from the user and write it to the file

# file1 = open('file_exsercise.txt',"w")
# Name = input("Enter your Name: ")
# file1.write(f'{Name} ')
# City = input("Enter City: ")
# file1.write(f'{City}')
# file1.close()

## 2: write a program to read from a file and write to another file 

# file1 = open('file_exsercise.txt',"r")
# # print(file1.readlines())
# print(file1.read())
# file2 = open('copy_file_exsercise',"w")
# for i in file1:
#     file2.write(i)
    
## 3: Write a program to read from a file and modify eacf of its line
## by pre-pending each line with "DIOT-" 

# file1 = open('file_exsercise.txt',"r")
# # file1 = open('file_exsercise.txt',"w")
# lst =[]
# for i in file1:
#     # print(i)
#     lst.append("Diot "+i)
# print(lst)

# file1 = open('file_exsercise.txt',"w")
# for i in lst:
#     file1.write(i)
    
    
    
## 4: Write a program to read from a file, pre-pending each line with "DIOT-" 
## and write to the different file


file1 = open('file_exsercise.txt',"r")
# file1 = open('file_exsercise.txt',"w")
lst =[]
for i in file1:
    # print(i)
    lst.append("Diot "+i)
print(lst)

file1 = open('file_exsercise.txt',"w")
for i in lst:
    file1.write(i)
    

# file2 = open('copy_file_exsercise.txt',"w") 
# for i in file2:
#     file2.write(i)





   
    
    