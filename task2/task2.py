p = []
with open('data(2).txt', 'r') as file1:
    c = file1.read()
for l in c.splitlines():
    p.append(l)
print(p)
with open('data.txt', 'r') as sfile1:
    d = sfile1.readline()
    d2 = d.split()
    x = float(d2[0])
    y = float(d2[1])
    print(x, y)
    d3 = sfile1.readline()
    r = float(d3[0])
for n in p:
    p2 = n.split()
    a = float(p2[0])
    b = float(p2[1])
    r2 = (x - a)**2 + (y - b)**2
    if r2 < r**2:
        print('Точка принадлежит кругу')
    elif r2 == r**2:
        print('Точка лежит на окружности')
    elif r2 > r**2:
        print('Точка снаружи')