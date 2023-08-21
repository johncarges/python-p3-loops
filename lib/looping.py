#!/usr/bin/env python3

def happy_new_year():
    for i in range(10,0,-1):
        print(i)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    return [i**2 for i in int_list]
    pass

def fizzbuzz():
    for i in range(1,101):
        string = ""
        if i%3 == 0:
            string += "Fizz"
        if i%5 == 0:
            string += "Buzz"
        if string == "":
            print(i)
        else:
            print(string)    
    pass
