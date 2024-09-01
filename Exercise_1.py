import random

def roll_dice():
    """Returns a random dice roll between 1 and 6."""
    return random.randint(1, 6)

def main():
    """Main program to roll the dice until the result is 6."""
    while True:
        result = roll_dice()  # Roll the dice
        print(f"Rolled: {result}")  # Print the result of the roll
        if result == 6:
            print("You rolled a 6! Exiting.")
            break  # Exit the loop if the result is 6

# Run the main program
if __name__ == "__main__":
    main()
