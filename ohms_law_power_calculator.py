
# ==========================================
# OHM'S LAW AND POWER CALCULATOR
# CTE123 PYTHON MINI PROJECT
# ==========================================

# Function to collect valid numerical input.
def get_number(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Invalid input! Enter a positive number.")

            elif value == 0 and not allow_zero:
                print("This value cannot be zero. Try again.")

            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to display the calculator menu.
def show_menu():
    print("\n===== OHM'S LAW AND POWER CALCULATOR =====")
    print("1. Calculate Voltage (V)")
    print("2. Calculate Current (I)")
    print("3. Calculate Resistance (R)")
    print("4. Calculate Power (P)")
    print("5. View Calculation History")
    print("0. Exit")
    print("==========================================")


# Function to display all electrical values.
def circuit_summary(voltage, current, resistance, power):

    print("\n===== COMPLETE CIRCUIT SUMMARY =====")
    print(f"Voltage:    {voltage:.2f} V")
    print(f"Current:    {current:.2f} A")

    if resistance is None:
        print("Resistance: Undefined")
    else:
        print(f"Resistance: {resistance:.2f} ohms")

    print(f"Power:      {power:.2f} W")
    print("====================================")


# Function to perform calculations.
def calculate(choice):

    if choice == "1":

        # Formula: V = I x R
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (ohms): ", False)

        voltage = current * resistance
        power = voltage * current

        answer = f"Voltage = {voltage:.2f} V"

    elif choice == "2":

        # Formula: I = V / R
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (ohms): ", False)

        current = voltage / resistance
        power = voltage * current

        answer = f"Current = {current:.2f} A"

    elif choice == "3":

        # Formula: R = V / I
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ", False)

        resistance = voltage / current
        power = voltage * current

        answer = f"Resistance = {resistance:.2f} ohms"

    elif choice == "4":

        # Formula: P = V x I
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")

        power = voltage * current

        # Calculate resistance where possible.
        if current == 0:
            resistance = None
        else:
            resistance = voltage / current

        answer = f"Power = {power:.2f} W"

    else:
        return None

    return voltage, current, resistance, power, answer


# Main function.
def main():

    # List for storing previous calculations.
    history = []

    print("WELCOME TO OHM'S LAW AND POWER CALCULATOR")

    # Loop keeps the program running.
    while True:

        show_menu()

        choice = input("Choose an option (0-5): ").strip()

        if choice == "0":

            print("\nThank you for using the calculator.")
            print("Goodbye!")
            break

        elif choice in ["1", "2", "3", "4"]:

            result = calculate(choice)

            voltage, current, resistance, power, answer = result

            print("\nCALCULATION RESULT:")
            print(answer)

            # Display the complete circuit summary.
            circuit_summary(
                voltage,
                current,
                resistance,
                power
            )

            # Save the calculation in history.
            history.append(answer)

        elif choice == "5":

            if len(history) == 0:
                print("\nNo calculations have been made yet.")

            else:
                print("\n===== CALCULATION HISTORY =====")

                for number, item in enumerate(history, start=1):
                    print(f"{number}. {item}")

                print("================================")

        else:

            print("\nInvalid option!")
            print("Please select a number from 0 to 5.")


# Start the program.
if __name__ == "__main__":
    main()
  
