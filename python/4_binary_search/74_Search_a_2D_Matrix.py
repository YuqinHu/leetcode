class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix[0])
        n = len(matrix)
        r = m * n - 1
        l = 0
        
        while l <= r:
            mid = (r + l) // 2
            i = mid // m
            j = mid % m
            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                return True
        return False