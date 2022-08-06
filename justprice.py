import math

def tax(n):
    return math.floor(n * 0.1)
def gensen(n):
    return math.floor(n * 0.1021)
def nice1(n):
    return n % 10 == 0
def nice2(n):
    return n % 100 == 0
def nice3(n):
    return n % 1000 == 0

total = 200000
start = 90000
center = int(total / 2)
asobi = 1000

for i in range(start, center+1):
    itax = tax(i)
    iaddtax = i + itax
    igensen = gensen(i)
    iseikyu = iaddtax - igensen
    for j in range(start-tax(start)-gensen(start), total-start):
        jtax = tax(j)
        jaddtax = j + jtax
        jgensen = gensen(j)
        jseikyu = jaddtax - jgensen

        ij = i + j
        ijtax = itax + jtax
        ijaddtax = iaddtax + jaddtax
        ijgensen = igensen + jgensen
        ijseikyu = iseikyu + jseikyu

        npoout = ijseikyu + ijgensen

        # if ij == total:
        if (ijaddtax >= total) and (ijaddtax <= total+asobi):
        # if ijseikyu == total:
        # if npoout == total:
        # if iseikyu + jseikyu == total: # if iaddtax + jaddtax == total:
        # if nice3(iseikyu) and nice3(jseikyu) and nice2(i) and nice2(j):
            if nice3(iseikyu) and nice3(jseikyu):
                # if nice1(iaddtax) and nice1(jaddtax):
                    print("[i:%d itax:%d iaddtax:%d igensen:%d iseikyu:%d]" % (i, itax, iaddtax, igensen, iseikyu))
                    print("[j:%d jtax:%d jaddtax:%d jgensen:%d jseikyu:%d]" % (j, jtax, jaddtax, jgensen, jseikyu))
                    print("(ij:%d ijtax:%d ijaddtax:%d ijgensen:%d ijseikyu:%d npoout:%d)" % (ij, ijtax, ijaddtax, ijgensen, ijseikyu, npoout))
                    print("")
