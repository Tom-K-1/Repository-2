
last_number = 1
second_to_last_number = 0
target = int(input("Enter a Number: "))
if (target == 1):
    print(0)
    exit()
if (target == 2):
    print(1)
    exit()
def Fib(count):
    global last_number, second_to_last_number, target
    temp = last_number
    last_number = last_number + second_to_last_number
    second_to_last_number = temp
    
    if (target > count):
        Fib(count + 1)
    else:
        print (last_number)
Fib(3)
