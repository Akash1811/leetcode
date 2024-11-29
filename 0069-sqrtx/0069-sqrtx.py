class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x
        while l<=r:
            m=(l+r)//2
            msqre=m*m
            if msqre==x:
                return m
            elif msqre<x:
                l=m+1
            else:
                r=m-1
        return r
        