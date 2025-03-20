#!/usr/bin/env python3

def greet_programmer():
    my_greeting = "Hello, programmer!"
    print(my_greeting)
    return my_greeting
greet_programmer()


def greet(name):
    print(f"Hello, {name}!")
    return name
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return name
greet_with_default()


def add(num1, num2):
    sum =(num1 + num2)
    print(sum)
    return sum
add(1,2)

def halve(number):
    result =(number / 2)
    print(result)
    return result
halve(4)


