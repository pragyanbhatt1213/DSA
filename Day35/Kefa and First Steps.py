n=int(input())
nums=list(map(int, input().split()))
max_len=1
curr_len=1
for i in range(len(nums)-1):
    if(nums[i+1]>=nums[i]):
        curr_len+=1
    if(nums[i+1]<nums[i]):
        curr_len=1
    max_len=max(curr_len,max_len)
print(max_len)
