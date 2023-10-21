import temperature_converter
def display_title():
    print("Temperature Converter")

def display_main():
    print("Choose an option:")
    print("1: Fahrenheit to Celsius")
    print("2: Celsius to Fahrenheit")
    print("3: Quit")

def main():
    while True:
        display_title()
        display_main()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            fahrenheit = float(input("Enter temperature (in Fahrenheit): "))
            celsius = temperature_converter.fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is approximately {celsius}°C")
        elif choice == '2':
            celsius = float(input("Enter temperature (in Celsius): "))
            fahrenheit = temperature_converter.celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is approximately {fahrenheit}°F")
        elif choice == '3':
            print("End of Program")
            print("Thank You, Good Bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3")

if __name__== "__main__":
    main()