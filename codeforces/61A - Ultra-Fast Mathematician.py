s1 = input()
s2 = input()
result = ''

for i in range(len(s1)):
    if s1[i] == s2[i]:
        result += '0'
    else:
        result += '1'
print(result)

