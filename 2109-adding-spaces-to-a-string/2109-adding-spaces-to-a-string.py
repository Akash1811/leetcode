class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        spaceindex=0
        for i in range(len(s)):
            if spaceindex<len(spaces) and i==spaces[spaceindex]:
                res.append(" ")
                spaceindex+=1
            res.append(s[i])
        return ''.join(res)
        