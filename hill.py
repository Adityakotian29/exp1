def hill_climb(arr, i):
    if i <= 0 or i >= len(arr) - 1:  # Base case: out of bounds
        return arr[i]  # Return the current element if it's out of bounds
    if arr[i - 1] > arr[i]:  # Check if the left neighbor is greater
        return hill_climb(arr, i - 1)  # Move left
    elif arr[i + 1] > arr[i]:  # Check if the right neighbor is greater
        return hill_climb(arr, i + 1)  # Move right
    return arr[i]  # Local maximum found

a = [1, 3, 2, 8, 6, 4, 5, 6, 7, 1, 9]  # Sample array
start_index = 5  # Starting index for hill climbing
local_maximum = hill_climb(a, start_index)  # Call the hill climbing function
print("Starting index:", start_index)  # Print starting index
print("Local maximum found:", local_maximum)  # Print the local maximum
