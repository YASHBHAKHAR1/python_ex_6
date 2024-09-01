def remove_odd_numbers(numbers):
    """Returns a new list with all odd numbers removed from the original list."""
    # Use list comprehension to filter out odd numbers
    return [num for num in numbers if num % 2 == 0]


def main():
    """Main program to test the remove_odd_numbers function."""
    # Create a sample list of integers
    original_list = [10, 15, 22, 33, 40, 57, 68]

    # Call the function to remove odd numbers
    filtered_list = remove_odd_numbers(original_list)

    # Print out the original and filtered lists
    print("Original list:", original_list)
    print("Filtered list (only even numbers):", filtered_list)


# Run the main program
if __name__ == "__main__":
    main()
