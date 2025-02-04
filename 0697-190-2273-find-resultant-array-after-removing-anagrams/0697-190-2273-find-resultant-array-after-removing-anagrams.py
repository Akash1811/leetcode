class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        seen_sorted_strings=set()
        result=[]
        prev_word = ""
        for word in words:
            if sorted(word) != sorted(prev_word):
                result.append(word)
                prev_word = word  
        return result
        