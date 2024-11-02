# Lab3.py
print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    # Copy input list to results list
    arr_result = arr.copy()
    # Get number of elements in the list
    n = len(arr_result)

    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                else:
                    return []
    return arr_result

def validate_and_sort(arr_input_list):
    # Check for empty input
    if not arr_input_list:
        return 0  # Zero numbers entered

    # Validate input before converting to integers
    all_integers = True
    for num in arr_input_list:
        if not num.strip().isdigit():
            all_integers = False
            break

    if not all_integers:
        return 2  # Invalid input (non-integer)

    # Convert strings to integers
    arr = [int(num.strip()) for num in arr_input_list if num.strip().isdigit()]

    # Check the number of elements entered
    if len(arr) >= 10:
        return 1  # More than or equal to 10 numbers

    return arr

def main():
    arr_input = input("Enter numbers separated by commas: ")
    arr_input_list = arr_input.split(",")
    result = validate_and_sort(arr_input_list)

    if result == 0:
        print("Zero numbers entered")
    elif result == 2:
        print("Invalid input! Please enter only integers.")
    elif result == 1:
        print("Do not enter more than 10 numbers!")
    else:
        # Sort in ascending order
        print("\nSorted array in ascending order:")
        print(bubble_sort(result, SORT_ASCENDING))
        # Sort in descending order
        print("Sorted array in descending order:")
        print(bubble_sort(result, SORT_DESCENDING))

if __name__ == "__main__":
    main()

