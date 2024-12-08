class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if not len(s) == len(goal):
            return False
        add=s+s
        return goal in add
        