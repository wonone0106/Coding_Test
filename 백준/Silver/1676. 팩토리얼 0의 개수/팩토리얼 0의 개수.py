n = int(input())
sum = 1
for i in range(2, n+1):
    sum *= i


count = 0
return_list = str(sum)[::-1]

for i in return_list:
    if i == '0':
        count += 1
    else:
        break

print(count)
