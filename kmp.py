# def compute_prefix_function(pattern):
#     m = len(pattern)
#     pi = [0] * m
#     k = 0
#     for q in range(1, m):
#         while k > 0 and pattern[k] != pattern[q]:
#             k = pi[k - 1]
#         if pattern[k] == pattern[q]:
#             k += 1
#         pi[q] = k
#     print(pi)
#     return pi
     

# def kmp_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     pi = compute_prefix_function(pattern)
#     q = 0
#     indices = []
#     for i in range(n):
#         while q > 0 and pattern[q] != text[i]:
#             q = pi[q - 1]
#         if pattern[q] == text[i]:
#             q += 1
#         if q == m:
#             indices.append(i - m + 1)
#             q = pi[q - 1]
#     return indices

# # Example usage
# text = "ababcababcabcabcab"
# pattern = "abcabc"
# print(kmp_search(text, pattern))  # Output: [5, 10, 15]

def fail(t):
    pi = [0] * len(t)
    for i in range(1, len(t)):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            pi[i] = j + 1
    return pi

def kmp_search(s, t):
    pi = fail(t)
    lmao = []
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != t[j]:
            j = pi[j - 1]
        if s[i] == t[j]:
            if j == len(t) - 1:
                lmao.append(i - j)
                j = pi[j]
            else:
                j += 1
    return lmao

s = 'iamnotgay'
t = 'gay'
print(kmp_search(s, t))
