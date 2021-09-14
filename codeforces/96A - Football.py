s = input()
contiguous = 1
answer = 'NO'
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        contiguous += 1
        if contiguous == 7:
            answer = 'YES'
            break
    else:
        contiguous = 1

print(answer)

