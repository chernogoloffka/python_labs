s = input()
i = 0
while not s[i].isupper():
    i += 1
start = i
j = start + 1
while not s[j].isdigit():
    j += 1
step = j - start + 1
result = ""
pos = start
while pos < len(s) and s[pos] != '.':
    result += s[pos]
    pos += step
result += "."
print(result)