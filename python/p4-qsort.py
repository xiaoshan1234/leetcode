

def qsort_k(nums, start:int, end:int , k:int) -> int:
    
    if start >= end:
        return nums[k]

    tmp = nums[start]
    i=start
    j=end
    while i<j:
        while i<j and nums[j]<=tmp:
            j=j-1
        nums[i] = nums[j]
        while i<j and nums[i]>=tmp:
            i=i+1
        nums[j] = nums[i]

    nums[i] = tmp

    if i == k:
        return tmp
    elif i<k:
        return qsort_k(nums,i+1,end,k)
    elif i>k:
        return qsort_k(nums,start,i-1,k)
        
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return qsort_k(nums, 0, len(nums)-1,k-1)