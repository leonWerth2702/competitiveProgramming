s = input()
t = input()

result = list(s)

for i in reversed(range(len(s))):
    if s[i] != 'z':
        result[i] = chr(ord(s[i]) + 1)
        break
    else:
        result[i] = 'a'

result = ''.join(result)

print(result if result != t else 'No such string')

