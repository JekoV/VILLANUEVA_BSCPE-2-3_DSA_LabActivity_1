def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_resistance(voltage, current):
    return voltage / current

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

def ohms_law_calculator():
    while True:
        print("\nWhat would you like to calculate?")
        print("a. Voltage (V)")
        print("b. Current (I)")
        print("c. Resistance (R)")
        choice = input("Enter a, b, or c: ").lower()

        if choice == 'a':
            current = get_valid_input("Enter the current (I) in amperes: ")
            resistance = get_valid_input("Enter the resistance (R) in ohms: ")
            voltage = calculate_voltage(current, resistance)
            print(f"The voltage (V) is: {voltage:.2f} volts")

        elif choice == 'b':
            voltage = get_valid_input("Enter the voltage (V) in volts: ")
            while True:
                resistance = get_valid_input("Enter the resistance (R) in ohms: ")
                if resistance == 0:
                    print("Resistance cannot be zero. Please enter a valid value.")
                else:
                    current = calculate_current(voltage, resistance)
                    print(f"The current (I) is: {current:.2f} amperes")
                    break

        elif choice == 'c':
            voltage = get_valid_input("Enter the voltage (V) in volts: ")
            while True:
                current = get_valid_input("Enter the current (I) in amperes: ")
                if current == 0:
                    print("Current cannot be zero. Please enter a valid value.")
                else:
                    resistance = calculate_resistance(voltage, current)
                    print(f"The resistance (R) is: {resistance:.2f} ohms")
                    break

        else:
            print("Invalid choice. Please enter a, b, or c.")
            continue 

        while True:
            convert_again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if convert_again == 'yes':
                break  
            elif convert_again == 'no':
                print("Thank you for using my Ohm's law calculator!")
                return  
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

ohms_law_calculator()


