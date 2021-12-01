inp = [int(x) for x in open("in1.txt").read().split()]
print(len([1 for a,b in zip(inp, inp[1:]) if a < b]))

x = [a+b+c for a,b,c in zip(inp, inp[1:], inp[2:])]
y = [a+b+c for a,b,c in zip(inp[1:], inp[2:], inp[3:])]
print(len([1 for a,b in zip(x, y) if a < b]))
