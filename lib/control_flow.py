#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    # your code here
    

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"

def fizzbuzz(num):
    if num % 3 ==0 and num % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
fizzbuzz(3)

def calculator(operation, num1, num2):
    if operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2
    elif operation == "-":
        return num1 - num2
    elif operation == "+":
        return num1 + num2
    else:
        print("Invalid operation!")
        return None
        

    # your code here
    
