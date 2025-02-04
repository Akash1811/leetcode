class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        add_s=s+s
        return s in add_s[1:-1]
        