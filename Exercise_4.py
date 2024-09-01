def sum_of_list(numbers):
    """Returns the sum of all integers in the list."""
    total = 0
    for number in numbers:
        total += number
    return total


def main():
    """Main program to test the sum_of_list function."""
    # Create a sample list of integers
    sample_list = [5, 15, 25, 35, 45]

    # Call the function to get the sum
    result = sum_of_list(sample_list)

    # Print out the result
    print(f"The sum of the list {sample_list} is {result}.")


# Run the main program
if __name__ == "__main__":
    main()
