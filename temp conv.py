def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    while True:
        print("Select the conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        conversion_type = input("Enter a or b: ")

        if conversion_type not in ['a', 'b']:
            print("Invalid input! Please choose between a or b.")
            continue  

        while True:
            try:
                temperature = float(input("Enter the temperature to be converted: "))
                break  
            except ValueError:
                print("Invalid temperature! Please enter a valid numerical value.")

        if conversion_type == 'a':
            converted_temp = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
        elif conversion_type == 'b':
            converted_temp = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")

        convert_again = input("Do you want to convert another temperature? (yes/no): ").lower()
        if convert_again != 'yes':
            print("Thank you! come again.")
            break 
        
temperature_converter()
