from art import calc
print(calc)
def calculate(a, b):
    selct = input("select the operation\n Press 1 for(+) \n Press 2 for(-) \n Press 3 for(x) \n Press 4 for(/) \n")
    if selct in ["1"]:
       z = print(a + b)
    if selct in ["2"]:
       z = print(a - b)    
    if selct in ["3"]:
       z = print(a * b)    
    if selct in ["4"]:
       z = print(a / b) 
    return z

x = int(input("Type the 1st no\n"))
y = int(input("Type the 2nd no\n"))
calculate(x, y)   

    
    
