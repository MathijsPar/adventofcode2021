#1
inp = ''.join(int(x[-1])*x[0] for x in open("in2.txt").read().strip().split('\n'))
print((inp.count('d')-inp.count('u'))*inp.count('f'))

#2
inp = [x.strip().split() for x in open("in2.txt")]
coords = [0,0]
aim = 0

for d,m in inp:
    m = int(m)
    if d[0] == 'f':
        coords[0] += aim*m
        coords[1] += m
    elif d[0] == 'd':
        aim += m
    elif d[0] == 'u':
        aim -= m

print(coords[0]*coords[1])
