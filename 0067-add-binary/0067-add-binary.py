class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        while b:
            withoutcarry=a^b
            carry=(a&b)<<1
            a,b=withoutcarry,carry
        return bin(a)[2:]
        