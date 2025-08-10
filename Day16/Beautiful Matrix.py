mat=[]
for _ in range(5):
    row=list(map(int,input().split()))
    mat.append(row)

for i in range(5):
    for j in range(5):
        if(mat[i][j]==1):
            print(abs((2-i))+abs((2-j)))
