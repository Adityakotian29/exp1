# def longest_common_subsequence(str1, str2):

#     m = len(str1)
#     n = len(str2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
    

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#     lcs = ""
#     i, j = m, n
#     while i > 0 and j > 0:
#         if str1[i - 1] == str2[j - 1]:
#             lcs = str1[i - 1] + lcs
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1

#     return lcs


# str1 = "ABCDGH"
# str2 = "AEDFHR"
# print("Longest Common Subsequence:", longest_common_subsequence(str1, str2))


s1 = input('Enter s1: ')
s2 = input('Enter s2: ')
n = len(s1)
m = len(s2)
sol = [[0] * (m + 1) for a in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            sol[i][j] = sol[i - 1][j - 1] + 1
        else:
            sol[i][j] = max(sol[i - 1][j], sol[i][j - 1])

lcs = ''
i, j = n, m
while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:
        lcs = s1[i - 1] + lcs
        i -= 1
        j -= 1
    elif sol[i - 1][j] > sol[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(sol[n][m])
print( lcs)
