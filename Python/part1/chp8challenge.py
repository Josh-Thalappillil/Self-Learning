#I challenge you to write three functions in a module, and use them in another Python program.
import challengechp7
import easycalc

challengechp7.guessgame()
num = easycalc.calc()

updated_num = easycalc.minus(num)

print(updated_num)