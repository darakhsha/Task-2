def primenumber(x,y):
    m= min(x,y)
    n= max(x,y)
    while m<=n:
        i=2
        while i<=m//2:
            if m%i==0:
                break
            i+=1
        if i>m//2:
            print(m,end=" ")
        m+=1
primenumber(1,5)