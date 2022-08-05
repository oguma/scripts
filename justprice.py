import math

total = 200000
step = 1

def wtax(n):
    return math.floor(n * 1.1)

def chk(n):
    return n % 100 == 0

def gensen(n):
    return math.floor(n * 0.1021)

for i in range(86000, total+1, step):
    a = wtax(i)
    for j in range(a, total+1, step):
        b = wtax(j)
        ig = gensen(i)
        jg = gensen(j)
        c = a - ig
        d = b - jg
        # s = a + b
        s = c + d
        if s == total:
            # if c(i) and c(j) and c(a) and c(b):
            # if chk(a) and chk(b):
            # if chk(i) or chk(j) or chk(a) or chk(b) or chk(c) or chk(d):
            if chk(c) and chk(d):
                # print(i, a, j, b, s, c, d)
                print("[unit:%d wtax:%d gensen:%d seikyu:%d] [unit:%d wtax:%d gensen:%d seikyu:%d] (seikyutotal:%d gensentotal:%d, npoout:%d)" % (i,a,ig,c,  j,b,jg,d, c+d,ig+jg,c+d+ig+jg))
