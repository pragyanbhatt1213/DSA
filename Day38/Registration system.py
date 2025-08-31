n=int(input())
db={}
for i in range(n):
    x=input()
    if(x not in db):
        db[x]=1
        print("OK")
    else:
        new=x+str(db[x])
        while new in db:
            db[x]+=1
            new=x+str(db[x])
        print(new)
        db[x]+=1       

