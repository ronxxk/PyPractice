import threading
import time

def p1():
    
    start_time = time.perf_counter()
    while True:
        inp = str(input("Nearest Planet?").lower())
        
        if inp == "venus":
            end_time = time.perf_counter()
            print(f"You are Right. Your Score is {round(end_time - start_time, 4)}\n")
            break
        else:
            print("Wrong Answer. Try again\n")
            
def p2():
    start_time = time.perf_counter()
    while True:
        inp = str(input("Nearest Planet?").lower())
        
        if inp == "venus":
            end_time = time.perf_counter()
            print(f"You are Right. Your Score is {round(end_time - start_time, 4)}\n")
            break
        else:
            print("Wrong Answer. Try again\n")
    


c1 = threading.Thread(p1())
c1.start()
c2 = threading.Thread(p1())
c2.start()

c1.join()
c2.join()