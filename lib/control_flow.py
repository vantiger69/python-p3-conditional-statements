#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
      return"Access granted"  
     
    else:
     
     return"Access denied"

admin_login("sudo","12345")
admin_login("admin","12345")
admin_login("ADMIN","12345")

    
def hows_the_weather(temperature):
    # your code here
    if  temperature < 40 :
       return "It's brisk out there!"
    elif temperature > 40 and temperature < 65 :
       return "It's a little chilly out there!"
    elif temperature > 85 :
       return "It's too dang hot out there!"
    else:
       print("It's perfect out there!")
hows_the_weather(39)
hows_the_weather(42)
hows_the_weather(99)
hows_the_weather(57)
   

def fizzbuzz(num):
    # your code here

    if num % 3 == 0 and num % 5 == 0:
      return "FizzBuzz"
    elif num % 3 == 0:
     return "Fizz"
    elif num % 5 == 0:
      return "Buzz"
    else:
      return num
 
fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)


def calculator(operation, num1, num2):
    # your code here
    if operation == "+" or operation == "-" or operation == "/" or operation == "*":
     if operation == "+":
      return num1 + num2
     elif operation == "-":
      return num1 - num2
     elif operation == "*":
      return num1 * num2
     elif operation == "/":
        if num2!=0:
         return num1 / num2
        else:
          return "Cannot divide by zero"
    else:
         return"None"
answer = calculator("+",1,1)
print(answer)
answer = calculator("-",3,1)
print(answer)

answer = calculator("*",3,2)
print(answer)

answer = calculator("/",4,2)
print(answer)

answer = calculator("nope",4,2)
print(answer)
