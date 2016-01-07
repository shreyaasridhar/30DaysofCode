import math
t=int(raw_input())
for i in range(0,t):
    x=map(int,raw_input().split())
    sum=x[0]
    for j in range(x[2]):
        sum+=math.pow(2,j)*x[1]
        print str(int(sum)) ,    
    print ''        