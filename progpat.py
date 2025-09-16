n=int(input())
k=1
x=1
for i in range(n):
    if n-k-1==-1:
        break
    if x==1:
        for i in range(2*n-1):
            print(n,end="")
            x=0
        print()
    d=0
    for i in range(n,n-k-1,-1):
        d+=1
        print(i,end="")
    w=0
    z=n
    q=1
    while(d<n):
        print(i,end="") 
        w+=1
        q=0
        d+=1
        z=i
        p=i
    if q==1 :
        for i in range(2,n+1):
            print(i,end="")
        print()
        break
    for i in range(w-1):
        print(z,end="")
    for i in range(z,n+1):
        print(i,end="")
    print()
    k+=1

t=1
c=1
for i in range(n-1):
    for i in range(n,t,-1):
        print(i,end="")
        h=i
        x=i
    for i in range(2*c):
        print(h,end="")
    for i in range(x+1,n+1):
        print(i,end="")
    print()
    t+=1
    c+=1

