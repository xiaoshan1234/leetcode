def b_search(nums,start,end,v):
    if start > end:
        return -1
    elif nums[start] == v:
        return start
    elif nums[end] == v:
        return end
    
    k = (start+end)//2
    while k>start and k<end:
        if v == nums[k]:
            return k
        elif v<nums[k]:
            k = (start+k)//2
        elif v>nums[k]:
            k = (k+end+1)//2

    return -1

def bz_search(nums,start,end,v):
    if start > end:
        return -1
    
    k = (start+end)//2
    
    if nums[k]==v:
        return k
    elif nums[start]==v:
        return start
    elif nums[end]==v:
        return end
    elif v<nums[k] and v > nums[start]:
        return b_search(nums,start,k-1,v)
    elif v>nums[k] and v < nums[end]:
        return b_search(nums,k+1,end,v)
    elif nums[k] <= nums[start]:
         return bz_search(nums,start,k-1,v)
    elif nums[k] >= nums[end]:
         return bz_search(nums,k+1,end,v)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
         return bz_search(nums,0,len(nums)-1,target)