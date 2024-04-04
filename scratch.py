val = 10

print(__name__)
if __name__ =="__main__":
    print("I was executed as main")
    print(val)
else:
    print("I was imported")
    

print(val)