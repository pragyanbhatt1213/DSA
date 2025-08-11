t= int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int,input().split()))
    over=0
    for i in range(n):
        if(a[i]>b[i]):
            over+=a[i]-b[i]

    loops=max(1,over+1)
    print(loops)

# for _ in range(t):
#     n=int(input())
#     a=list(map(int, input().split()))
#     b=list(map(int,input().split()))
#     count=0
#     while True:
#         count+=1
#         one=False
#         for i in range(n):
#             if(a[i]>b[i]):
#                 a[i]=a[i]-1
#                 one=True
#                 break
#         for i in range(n):
#             if(a[i]<b[i]):
#                 a[i]=a[i]+1
#                 break
#         if not one:
#             break
#     print(count)

                


