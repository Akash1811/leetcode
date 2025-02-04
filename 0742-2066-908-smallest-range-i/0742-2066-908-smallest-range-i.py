class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        small=min(nums)+k
        large=max(nums)-k
        return max(0,large-small)
        