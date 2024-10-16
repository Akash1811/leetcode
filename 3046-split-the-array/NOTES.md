nums.sort()
num1, num2 = [], []
for i in range(len(nums)):
if i % 2:
num2.append(nums[i])
else:
num1.append(nums[i])
return len(num1) == len(set(num1)) and len(num2) == len(set(num2))