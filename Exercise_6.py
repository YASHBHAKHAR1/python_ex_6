import math


def calculate_unit_price(diameter_cm, price_euros):
    """Calculate the unit price of a pizza per square meter.

    Args:
        diameter_cm (float): Diameter of the pizza in centimeters.
        price_euros (float): Price of the pizza in euros.

    Returns:
        float: Unit price per square meter.
    """
    # Convert diameter from cm to meters
    diameter_m = diameter_cm / 100.0

    # Calculate the radius in meters
    radius_m = diameter_m / 2

    # Calculate the area of the pizza in square meters
    area_m2 = math.pi * (radius_m ** 2)

    # Calculate and return the unit price per square meter
    return price_euros / area_m2


def main():
    """Main program to compare the unit price of two pizzas."""
    # Get the diameter and price of the first pizza
    diameter1 = float(input("Enter the diameter of the first pizza in centimeters: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    # Get the diameter and price of the second pizza
    diameter2 = float(input("Enter the diameter of the second pizza in centimeters: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    # Calculate unit prices per square meter
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    # Print the unit prices
    print(f"Unit price of the first pizza: {unit_price1:.2f} euros per square meter")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros per square meter")

    # Determine which pizza is a better deal
    if unit_price1 < unit_price2:
        print("The first pizza offers better value for money.")
    elif unit_price1 > unit_price2:
        print("The second pizza offers better value for money.")
    else:
        print("Both pizzas offer the same value for money.")


# Run the main program
if __name__ == "__main__":
    main()
