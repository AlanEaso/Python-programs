#Countdown Timer

from time import * #for using the sleep function from this package

#countdow functiom
def countdown(a):
    while(a):
        min, sec = divmod(a, 60)
        print("{:02d}:{:02d}".format(min,sec),end="\r")
        sleep(1) #waiting 1 second before decrementing
        a-=1
    print("Timer completed")

#Getting input from user
t = int(input("Enter the time in seconds : "))
countdown(t)