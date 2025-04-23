def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]
my_array = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
selection_sort(my_array)
print("Sorted array using Selection Sort:", my_array)


def recursive_selection_sort(arr, n):
    if n <= 1:
        return arr
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i

   
    arr[0], arr[min_index] = arr[min_index], arr[0]
    recursive_selection_sort(arr[1:], n - 1)
my_array = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
recursive_selection_sort(my_array, len(my_array))
print("Sorted array using Recursive Selection Sort:", my_array)

