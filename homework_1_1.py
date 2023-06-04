c = 0
f = 0

# from Celsius to Fahrenheit converter:

c = float(input("Please enter a temperature in Celsius: "))
f = (c*9/5)+32
a = '\u00b0'
print(f'A temperature of {c} {a}C is {f} {a}F.')

# from Fahrenheit to Celsius converter:

f = float(input("Please enter a temperature in Fahrenheit: "))
c = (f-32)*5/9

print(f'A temperature of {f} °F is {c} °C. ')
