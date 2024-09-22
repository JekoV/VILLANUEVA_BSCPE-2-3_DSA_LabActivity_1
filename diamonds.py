def print_diamond(n):
    if n % 2 == 0:
        print("Please provide an odd number to create a diamond figure.")
        return

    for i in range(n // 2 + 1):
        print(" " * ((n // 2) - i) + "*" * (2 * i + 1))

    for i in range(n // 2 - 1, -1, -1):
        print(" " * ((n // 2) - i) + "*" * (2 * i + 1))

while True:

    while True:
        try:
            n = int(input("Enter an odd number to create a diamond figure: "))
            if n % 2 == 0:
                print("That's an even number. Please enter an odd number.")
                continue
            break  
        except ValueError:
            print("Invalid input! Please enter a valid number (odd).")

    print_diamond(n)

    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("That's a whole lot of diamonds you got there!")
        break


