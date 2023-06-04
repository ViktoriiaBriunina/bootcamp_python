#c = 0
#f = 0

#c = float(input("Please enter a temperature in Celsius or Fahrenheit: "))
#f = (c*9/5)+32
#c = (f-32)*5/9

#print(f'A temperature of {c} in Celsius degree is {f} in Fahrenheit.') ...

while True:

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Please choose (1-3): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C is equal to {f}°F\n")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F is equal to {c}°C\n")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Your choice is invalid, please try again")


