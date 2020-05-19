# first set() (40%)
print("1:")
a = set([1, 12, 32, 74, 45, 16, 87])
b = set([12, 87, 55, 32, 16])
c = set([92, 87, 74, 55, 41, 23, 8])

i = list(a & b & c)
j = list(a & c)
k = list(a^b^c - set(i))
l = list(((a | b | c) - set(k))- set(i))

print (i)
print (j)
print (k)
print (l)

# second List (30%)
print("2:")
A = list(range(1,101))
ans = []
for index in A:
    if (index % 2 != 0) and (index % 3 != 0):
        ans.append(index)
print(A)
print(ans)
ans.sort(reverse=True)
print(ans)

#third Dictionary (30%)
print("3:")
s = "Cognitive radio (CR) can effectively alleviate the problems and catches a lot of attention in the world [2-3]."
p = [1, 1, 5, 2, 2, 1, 1, 3, 1, 2, 5, 1, 4, 4, 4, 1, 3, 3, 4, 4, 5, 1, 3, 2, 2, 3]
str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0 ,0 ,0 ,0 ,0 ,0, 0]

s=s.lower()
print(s)

for ch in s:
    if ch not in str_list:
        str_list.append(ch)
        count.append(0)

for ch in s:
    count[str_list.index(ch)]+=1

dictionary = dict(zip(str_list, count))
print({key:val for key, val in dictionary.items() if val != 0})

for i in range(len(p)):
    count[i] = count[i] * p[i]

dictionary = dict(zip(str_list, count))
print({key:val for key, val in dictionary.items() if val != 0})