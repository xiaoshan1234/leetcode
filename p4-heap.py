def heap_adjust(nums, start, end):
    if start>=end:
        return
    k=start
    sd=nums[k]
    i=2*k+1
    while i<=end:
        if i<end and nums[i]<nums[i+1]:
            i+=1
        if nums[i]>sd:
            nums[k] = nums[i]
            k=i
        else:
            break
        i=i*2+1
    nums[k]=sd        

def head_build(nums,length):
    for i in range((length-2)//2,-1,-1):
        heap_adjust(nums,i,length-1)
        
    
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        length = len(nums)
        head_build(nums,length)
        for i in range(0,k):
            tail = length-1-i
            t = nums[0]
            nums[0] = nums[tail]
            nums[tail] = t
            heap_adjust(nums,0,tail-1)

        return nums[length-1-(k-1)]
    
a= [9,4,6,0,8]
s=Solution()
s.findKthLargest(a,1)
