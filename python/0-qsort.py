import random

def qsort(nums, start:int, end:int) -> None:
    if start>=end:
        return 
    i=start
    j=end
    sp = nums[start]
    while i<j:
        while i<j and nums[j]>=sp:
            j=j-1
        nums[i] = nums[j]
        while i<j and nums[i]<=sp:
            i=i+1
        nums[j] = nums[i]

    nums[i] = sp
    
    qsort(nums,start,i-1)
    qsort(nums,i+1,end)

# a = [random.randint(0,1000) for i in range(100000)]
a = [9,4,6,0,8]
print(a)
qsort(a,0,len(a)-1)
print(a)