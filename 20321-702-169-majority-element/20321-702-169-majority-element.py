class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate,counter=None,0
        for num in nums:
            if counter==0:
                candidate=num
                counter=1
            elif num==candidate:
                counter+=1
            else:
                counter-=1
        count = nums.count(candidate)
        if count>len(nums)//2:
            return candidate
        else:
            return None
        
        
        