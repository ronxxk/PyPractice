from art import calc
print(calc)
def calculate(a, b):
    selct = input("select the operation\n Press 1 for(+) \n Press 2 for(-) \n Press 3 for(x) \n Press 4 for(/) \n")
    if selct in ["1"]:
       return a + b
    elif selct in ["2"]:
       return a - b    
    elif selct in ["3"]:
       return a * b    
    elif selct in ["4"]:
       return a / b 
    else:
        print("Invalid operation")
        return None


on = True
last_digit = None
while on:
    if last_digit == None:
       c = int(input("Type the 1st no\n"))
    else:
       c = last_digit
    
    d = int(input("Type the 2nd no\n"))
    result = calculate(c, d)
    if result is not None:
        print(result)
        last_digit = result
    Choice = str(input("Do you wanna continue with the last result? Y/N\n")).lower()
    if Choice != "y":
       on = False
     
    
    
