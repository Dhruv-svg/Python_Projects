import time

def countdown(n):
    if(n==0):
        print("Blast Off")

    else:
            print(n)
            time.sleep(1)
            countdown(n-1)

n = int(input("Enter the limit of the stopwatch"))
countdown(n)