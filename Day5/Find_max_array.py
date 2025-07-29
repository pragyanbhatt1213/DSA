#codechef
T= int(input())
for i in range(T):
    N= int(input())
    A = list(map(int, input().split()))
    max=A[0]
    for i in range(N):
        if(A[i]>max):
            max=A[i]
    print(max)
