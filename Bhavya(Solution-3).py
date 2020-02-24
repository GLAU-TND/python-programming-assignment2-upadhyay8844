s = int(input())
b = bin(s)
b = b[2::]
c=1
for i in range(len(b)-1):
    if b[i] == '1' and b[i+1] == '1':
        c += 1
print(c)
