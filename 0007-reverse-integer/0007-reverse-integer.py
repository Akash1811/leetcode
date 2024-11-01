class Solution:
    def reverse(self, x: int) -> int:
        is_neg=x<0
        x=abs(x)
        rev_num=0
        while x>0:
            rev_num=rev_num*10+x%10
            x//=10
        if is_neg:
            rev_num=-rev_num
        if rev_num<-2**31 or rev_num>2**31-1:
            return 0
        return rev_num