def qsort(nums, start:int, end:int) -> None:
    tmp = nums[start]
    i=start
    j=end
    if start>=end:
        return 
    
    while i<j:
        while i<j and nums[j]>=tmp:
            j=j-1
        nums[i] = nums[j]
        while i<j and nums[i]<=tmp:
            i=i+1
        nums[j] = nums[i]

    nums[i] = tmp
    
    qsort(nums,start,i-1)
    qsort(nums,i+1,end)