def iterative_merge_sort(arr):
    size = 1
    n = len(arr)

    while size < n:
        left = 0
        while left < n - 1:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            merge(arr, left, mid, right)

            left += 2 * size

        size *= 2

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_half = arr[left: left + n1]
    right_half = arr[mid + 1: mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1
my_array = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
iterative_merge_sort(my_array)
print("Sorted array using Iterative Merge Sort:", my_array)





def recursive_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        recursive_merge_sort(left_half)
        recursive_merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
my_array = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
recursive_merge_sort(my_array)
print("Sorted array using Recursive Merge Sort:", my_array)
