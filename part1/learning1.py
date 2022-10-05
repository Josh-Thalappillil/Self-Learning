#printing with a return
def maths(x):
    return x * 2
    

result = maths(2)
print(result)


#printing even or odd numbers using a function
def even_odd(x):
    if x % 2 == 0: print("even")
    else:
        print("odd")
even_odd(22) 
even_odd(35)

#parameters
def f():
    return 1 + 1

result = f()
print(result)

#multiple parameters
def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)