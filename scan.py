def scan(head, tracks, n):
    left = [i for i in tracks if i < head]
    left = sorted(left)
    right = [i for i in tracks if i > head]
    right = sorted(right)
    
    while True:
        print("1. Right\n2. Left")
        choice = input("Enter your choice: ")

        if choice == '1':
            l = n - head
            m = n - left[0]
            return l + m
        elif choice == '2':
            l = head - 0
            m = right[-1] - 0
            return l + m

# Example usage
tracks = [82, 170, 43, 140, 24, 16, 190]
head = 50
t = 200
n = t - 1
print("Total distance:", scan(head, tracks, n))


# def look(head, tracks, n):
#     left = [i for i in tracks if i < head]
#     left = sorted(left)
#     right = [i for i in tracks if i > head]
#     right = sorted(right)
    
#     while True:
#         print("1. Right\n2. Left")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             l = right[-1] - head
#             m = right[-1] - left[0]
#             return l + m
#         elif choice == '2':
#             l = head - left[0]
#             m = right[-1] - left[0]
#             return l + m

# # Example usage
# tracks = [82, 170, 43, 140, 24, 16, 190]
# head = 50
# t = 200
# n = t - 1
# print("seek distance:", look(head, tracks, n))


