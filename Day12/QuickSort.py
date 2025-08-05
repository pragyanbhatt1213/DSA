def quick_sort(arr):
    n=len(arr)
    if(n<=1):
        return(arr)
    else:
        pivot=arr.pop()
    greater=[]
    lower=[]

    for i in arr:
        if(i>pivot):
            greater.append(i)
        else:
            lower.append(i)
    return( quick_sort(lower) + [pivot] + quick_sort(greater))
arr=[6,2,4,1,3]
print(quick_sort(arr))
