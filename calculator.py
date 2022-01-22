
from colorama import init
from colorama import Fore, Back, Style

print(Fore.MAGENTA)
print("Привет это обычный калькулятор,можешь просто делать уравнения и писать уравнения с десятичным дробом.")
print(Fore.BLUE)
what = input( "какой у тебя знак уравнения?:" )
a = float( input("первое число: ") )
b = float( input("второе число: ") )
print(Fore.MAGENTA)
print(Style.BRIGHT)
if what == "+":
    equation = a + b
    print("Ответ: " + str(equation))
elif what == "-":	
	equation = a - b
	print("Ответ: " + str(equation))  
elif what == "*":
	  equation = a * b 
	  print("Ответ: " + str(equation))
elif what == "/":
	  equation = a / b
	  print("Ответ: " + str(equation))
else:
	print(Fore.RED)
	print("в этой программе еще нет такого знака")
	input()
	