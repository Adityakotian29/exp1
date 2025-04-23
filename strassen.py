def add(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

def sub(a, b):
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]

def mul(a, b):
   
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    mid = len(a) // 2
    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]
    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]


    p1 = mul(add(a11, a22), add(b11, b22))
    p2 = mul(add(a21, a22), b11)
    p3 = mul(a11, sub(b12, b22))
    p4 = mul(a22, sub(b21, b11))
    p5 = mul(add(a11, a12), b22)
    p6 = mul(sub(a21, a11), add(b11, b12))
    p7 = mul(sub(a12, a22), add(b21, b22))

 
    c11 = add(sub(add(p1, p4), p5), p7)
    c12 = add(p3, p5)
    c21 = add(p2, p4)
    c22 = add(sub(add(p1, p3), p2), p6)
    result = []
    for i in range(mid):
        result.append(c11[i] + c12[i])
    for i in range(mid):
        result.append(c21[i] + c22[i])
    return result

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print(mul(a, b))



