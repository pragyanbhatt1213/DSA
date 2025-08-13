
#Not optimized approach 
# rev=""
# for i in s:
#     rev=i+rev
# if(rev==t):
#     print("YES")
# else:
#     print("NO")
s=input()
t=input()
rev=s[::-1]
if(rev==t):
    print("YES")
else:
    print("NO")
