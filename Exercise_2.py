import random


def roll_dice(sides):
    """Returns a random dice roll between 1 and the number of sides."""
    return random.randint(1, sides)


def main():
    """Main program to roll the dice until the result is the maximum number."""
    try:
        # Ask the user for the number of sides on the dice
        sides = int(input("Enter the number of sides on the dice: "))

        if sides < 1:
            print("The number of sides must be at least 1.")
            return

        print(f"Rolling a {sides}-sided dice...")

        while True:
            result = roll_dice(sides)  # Roll the dice
            print(f"Rolled: {result}")  # Print the result of the roll
            if result == sides:
                print(f"You rolled a {sides}! Exiting.")
                break  # Exit the loop if the result is the maximum number

    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of sides.")


# Run the main program
if __name__ == "__main__":
    main()
