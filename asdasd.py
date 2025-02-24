"""
def greeting(name):
    print("Sveika," + name + "!")
    
    
greeting(" Anna")
"""
"""
def sum_numbers(a,b):
    return a + b
print(sum_numbers(5, 3))
"""
"""
def is_even(n):
    if n % 2 == 0:
        print ("True")
    else:
        print ("False")
(is_even(4))
(is_even(7))
"""
"""
def myFactorial(number = 0):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
    
faktorials = myFactorial(5)
print(faktorials)
def function(x):
        result = 3 * x + 2
        return result
"""
def fizzbuzz(n):
    result = []
    if i % 3==0 and i % 5 == 0:
        result.apend("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
        result.append("Buzz")
        else:
            result.append(str(i))
        return result
