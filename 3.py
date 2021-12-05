import numpy as np
from scipy import stats
#3.1
y=stats.mode(np.split(np.array([int(x) for x in open("in3.txt").read() if x.isdigit()]),1000)).mode
print(y.dot(1<<np.arange(y.shape[-1]-1,-1,-1))*(y^1).dot(1<<np.arange((y^1).shape[-1]-1,-1,-1)))
#3.2
inp = np.array(np.split(np.array([int(x) for x in open("in3.txt").read() if x.isdigit()]),1000))
def filteroxybits(c,t):
    if len(c)==1 or t.shape[1]==0:
        return c
    current=1 if sum(t[:,0])>=(c.shape[0]/2) else 0
    pos=c.shape[1]-t.shape[1]
    return filteroxybits(c[c[:,pos]==current],c[:,pos+1:])
def filterco2bits(c,t):
    if len(c)==1 or t.shape[1]==0:
        return c
    current=0 if sum(t[:,0])>(c.shape[0]/2) else 1
    pos=c.shape[1]-t.shape[1]
    return filteroxybits(c[c[:,pos]==current],c[:,pos+1:])
g=filteroxybits(inp,inp)
h=filterco2bits(inp,inp)
print(g,h)
print(g.dot(1<<np.arange(g.shape[-1]-1,-1,-1))*h.dot(1<<np.arange(h.shape[-1]-1,-1,-1)))
#attempt2
def filteroxy(c,r):
    if c.shape[1]==len(r):
        return r
    pos=len(r)-c.shape[1]
    cur=1 if sum(c[:,pos])>=c.shape[0]/2 else 0
    return filteroxy(c[c[:,pos]==cur],r+str(cur))
def filterco2(c,r):
    if c.shape[1]==len(r):
        return r
    pos=len(r)-c.shape[1]
    cur=0 if sum(c[:,pos])>c.shape[0]/2 else 1
    return filterco2(c[c[:,pos]==cur],r+str(cur))
print(int(filteroxy(inp,""),2)*int(filterco2(inp,""),2))
