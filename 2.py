inp = ''.join(int(x[-1])*x[0] for x in open("in2.txt").read().strip().split('\n'))
(inp.count('d')-inp.count('u'))*inp.count('f')