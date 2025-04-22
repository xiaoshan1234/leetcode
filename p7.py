class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rst = nums[0]
        prev = 0
        for i in range(len(nums)):
            dp = nums[i]+prev if nums[i]+prev>nums[i] else nums[i]
            rst = dp if rst<dp else rst
            prev = dp
        
        return rst