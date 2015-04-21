#coding=utf-8

for i in range(9,0,-1):
    for m in range(0,9-i):
        print ("\t", end='')
    for j in range(i,0,-1):
        u = str.format("%d*%d=%d\t" % (j, i, j*i))
        print (u, end='')
    print ('')
