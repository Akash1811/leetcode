class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        summ=""
        i=0
        j=0
        while i<len(word1)and j<len(word2):
            summ+=word1[i]+word2[j]
            i+=1
            j+=1
        summ+=word1[i:]+word2[j:]
        return summ