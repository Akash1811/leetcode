class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        matrix.reverse()
        for r in range(n):
            for c in range(r):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
                #matrix.reverse()
        """
        Do not return anything, modify matrix in-place instead.
        """
        