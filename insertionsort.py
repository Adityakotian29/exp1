# def iterative_insertion_sort(arr):
#     n = len(arr)

#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1

      
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key


# my_array = [int(x) for x in input("Enter array elements separated by spaces: ").split()]

# iterative_insertion_sort(my_array)
# print("Sorted array using Iterative Insertion Sort:", my_array)





# def recursive_insertion_sort(arr, n):
#     if n <= 1:
#         return arr
#     recursive_insertion_sort(arr, n - 1)

#     key = arr[n - 1]
#     j = n - 2

#     while j >= 0 and key < arr[j]:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key
# my_array = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
# recursive_insertion_sort(my_array, len(my_array))
# print("Sorted array using Recursive Insertion Sort:", my_array)

def insertion(lmao):
    n = len(lmao)
    for i in range(1, n):
        key = lmao[i]
        j = i - 1
        while j >= 0 and key < lmao[j]:
            lmao[j + 1] = lmao[j]
            j -= 1
        lmao[j + 1] = key
        print(lmao)

lmao = [12, 11, 13, 5, 6]
insertion(lmao)
print("Sorted array is:", lmao)
          