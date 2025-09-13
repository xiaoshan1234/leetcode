class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        s = set(nums)
        while i<len(nums):
            k = target-nums[i]
            if k in s:
                j=nums.index(k)
                if i!=j:
                    return [i,j]
            i+=1
            
            