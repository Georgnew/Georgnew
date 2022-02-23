print('n=')
n = int(input())
print('m=')
m = int(input())
a = []
if m == 0 or n == 0:
    print('Ошибка входных параметров')
a.append(1)
i=0
result=0
while (result==0):
    if i+m-1>=len(a):
        while i+m-1>=len(a):
            for j in range(1,n):
                a.append(j+1)
            a.append(1)
    print(a[i])
    i = i + m - 1
    if a[i]==1:
        result=1
print(a)