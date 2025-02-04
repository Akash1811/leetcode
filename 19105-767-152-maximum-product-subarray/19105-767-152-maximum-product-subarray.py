class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_pro=nums[0]
        max_pro=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                min_pro,max_pro=max_pro,min_pro
            max_pro=max(nums[i],max_pro*nums[i])
            min_pro=min(nums[i],min_pro*nums[i])
            res=max(res,max_pro)
        return res
        