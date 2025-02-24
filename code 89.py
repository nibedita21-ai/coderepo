def nearest_greater_to_right(arr):
    n = len(arr)  # Get the length of the array
    result = [-1] * n  # Initialize result list with -1 (default value)
    
    # Loop through each element in the array
    for i in range(n):
        for j in range(i + 1, n):  # Check elements to the right
            if arr[j] > arr[i]:  # Find the first greater element
                result[i] = arr[j]
                break  # Stop searching once the first greater element is found
    
    return result

# User input
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Find and print nearest greater elements
output = nearest_greater_to_right(arr)
print("Nearest Greater Elements to the Right:", output)
