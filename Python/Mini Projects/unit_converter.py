#Build a unit converter that can convert between different units of measurement
#(e.g., kilometers to miles, Celsius to Fahrenheit). This project will strengthen your
#understanding of functions and user input.

def km_to_miles(kminput):
    return (kminput / 1.60934)

def miles_to_km(milesinput):
    return (milesinput * 1.60934)

def c_to_f(cinput):
    return ((cinput * 1.8) + 32)

def f_to_c(finput):
    return ((finput - 32) / 1.8)

choice = (input("Input choice: "))

choice_input = float(input("Input your value: "))

if choice == "A":
    print(km_to_miles(choice_input))
elif choice == "B":
    print(miles_to_km(choice_input))
elif choice == "C":
    print(c_to_f(choice_input))
else:
    print(f_to_c(choice_input))

