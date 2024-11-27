class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        n=len(nums)
        for i in range(n):
            rightsum=total-nums[i]-leftsum
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1

        