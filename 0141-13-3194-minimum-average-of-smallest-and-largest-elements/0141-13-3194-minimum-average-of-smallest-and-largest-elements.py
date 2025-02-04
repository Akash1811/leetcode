class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
       nums.sort()
       avg=[]
       n=len(nums)
       for i in range(n//2):
        minele=nums[i]
        maxele=nums[n-i-1]
        average=(minele+maxele)/2
        avg.append(average)
       return(min(avg))



        