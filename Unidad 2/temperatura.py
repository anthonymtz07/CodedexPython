"""
TEMPERATURE
Computers are incredile at doing math calculations. Now that we have learned about variables, let's use them with 
arithmetic operatiors to calculate things!

Python has the following arithmetic operators:
* + Addition
* - Substraction
* * Multiplication
* / Division
* % Modulo (returns the remainder)

score = 0   #score is 0
score = 4 + 3   #score is now 7
score = 4 - 3   #score is now 1
score = 4 * 3   #score is now 12 
score = 4 / 3   #score is now 1.3333
score = 4 %     #score is now 1

And take a look at this code that calculates a 20% tip by calculating the total and then multiplying a float (decimal number):

pizza = 2.99 
cake = 0.99

total = total * 0.2 

print(tip) #Output: 0.796

Another way to write this is using parentheses to calculate the toal and the tip in the line of code: 

tip = (pizza + coke) * 0.2 

In python, parentheses have the highest orden of operations.

Now that we've learned about the basics of variables and operators, let's put them to use!

INSTRUCTIONS

Create a temperature.py program that convenrts a temperature from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Booklyn, NY (where Codedex is based) in °F

Use the following formula and write it out in Python: 

            (Fahrenheit - 32) 
Celsius = ------------------

Print out hte converted temperature

"""

def Celsius(temperature):
        total_F = temperature - 32
        total = total_F / 1.8 
        return total

celsius = Celsius(int(input('Temperatura a cambiar: ')))
print(celsius)




