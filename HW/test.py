"""
1. set()
"""

a = set([1, 12, 32, 74, 45, 16, 87])
b = set([12, 87, 55, 32, 16])
c = set([92, 87, 74, 55, 41, 23, 8])

print("1.")
print((a & b) & c)
print("2.")
print(a & c)
print("3.")
print((a ^ b) ^ c)
print("4.")
print( ( (a&b) | (b&c) | (a&c) ) - ((a & b) & c))

"""
2. List 操作
"""

A = []

for i in range( 1, 101):
    A.append( i)
print("1.")
print(A)

for i in range( 1, 101):
    if ( i%2 == 0) or ( i%3 == 0):
        A.remove( i)
print("2.")
print(A)

A.sort(reverse=True)

print("3.")
print(A)

"""
3. Dictionary 操作
"""

s = "Cognitive radio (CR) can effectively alleviate the problems and catches a lot of attention in the world [2-3]."
p = [1, 1, 5, 2, 2, 1, 1, 3, 1, 2, 5, 1, 4, 4, 4, 1, 3, 3, 4, 4, 5, 1, 3, 2, 2, 3]

S = s.lower()
print("1.")
print(S)

d = {}
for c in S:
    d[c] = d.get(c,0) + 1
print("2.")
print(d)

d2 = d.fromkeys( d, 0)
for c in S:
    if c.isalpha():
        d2[c] += p[ord(c) - 97]
    else:
        d2[c] += 1

print("3.")
print(d2)