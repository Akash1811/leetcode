class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        og=x
        while x>0:
            rev=rev*10+x%10
            x//=10
        return og==rev
        