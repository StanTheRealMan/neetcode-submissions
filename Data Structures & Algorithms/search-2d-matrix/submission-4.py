class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                l, r = 0, len(matrix[m]) - 1
                cur = m
                while l <= r:
                    m = l + (r - l) // 2
                    if matrix[cur][m] > target:
                        r = m - 1
                    elif matrix[cur][m] < target:
                        l = m + 1
                    else:
                        return True
                return False

        return False