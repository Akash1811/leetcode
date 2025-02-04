class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1:
            return 0
        nums.sort()
        ans=nums[n-1]-nums[0]
        for i in range(1,n):
            small=min(nums[0]+k,nums[i]-k)
            large=max(nums[n-1]-k,nums[i-1]+k)
            ans=min(ans,large-small)
        return ans
        