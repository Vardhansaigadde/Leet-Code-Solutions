class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        nums = [0]*n
        for i in range (n):
            sum = 0
            for j in range (n):
                sum += matrix[i][j]
            nums[i] = sum

        return nums        

