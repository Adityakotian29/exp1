def last_occurrence(t):
    set = {}
    for i, char in enumerate(reversed(t)):
        if char not in set:
            set[char] = len(t) - i - 1
    print(set)
    return set

def booyer(s,t):
    m = len(t)
    lmao = last_occurrence(t)
    for i in range(len(s)):
        j = m - 1
        while j >= 0 and s[i] == t[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += m - min(j, 1 + lmao.get(s[i], -1))
    return -1

s = 'iamnotgay'
t = 'gay'
print(last_occurrence(t))    
print(booyer(s,t))
print("changed")

  

    