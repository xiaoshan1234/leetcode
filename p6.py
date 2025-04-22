def qsort(nums,start,end):
    if start >= end:
        return
    sp = nums[start]
    i = start
    j = end
    while i<j:
        while i<j and sp<=nums[j]:
            j-=1
        nums[i] = nums[j]
        while i<j and sp>=nums[i]:
            i+=1
        nums[j] = nums[i]

    nums[i] = sp
    qsort(nums,start,i-1)
    qsort(nums,i+1,end)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        qsort(nums,0,len(nums)-1)
        i=0
        rst = []
        while i<len(nums)-2:
            j = i+1
            k = len(nums)-1
            while j<k:
                if j<k and nums[k]+nums[j]>-nums[i]:
                        k-=1 
                elif j<k and nums[j]+nums[k]<-nums[i]:
                        j+=1 
                elif j<k and nums[j]+nums[k]==-nums[i]:
                    rst.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
            i+=1
            while  i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1

        return rst
