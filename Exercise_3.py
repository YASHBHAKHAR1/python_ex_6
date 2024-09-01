def gallons_to_liters(gallons):
    """Converts gallons to liters."""
    liters_per_gallon = 3.78541
    return gallons * liters_per_gallon


def main():
    """Main program to convert gallons to liters until a negative value is entered."""
    while True:
        try:
            # Ask the user for the volume in gallons
            gallons = float(input("Enter the volume in gallons (negative value to quit): "))

            if gallons < 0:
                print("Negative value entered. Exiting.")
                break

            # Convert gallons to liters
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equivalent to {liters:.2f} liters.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Run the main program
if __name__ == "__main__":
    main()
