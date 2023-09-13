#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
 count = 10
 while count>=1:
      print(f'{count}')
      print("Happy New Year!")
      count -= 1
happy_new_year()

def square_integers(int_list):
    # code goes here!
 squared_integers=[integer**2 for integer in int_list]
 return squared_integers
 squared_list = square_integers([1,2,3,4,5])
 print(squared_integers)


def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i%3==0 and i%5==0:
         print ('FizzBuzz')
        elif i%3==0:
          print ('Fizz')
        elif i%5==0:
           print ('Buzz')
        else:
           print (f'{i}')
          
    
