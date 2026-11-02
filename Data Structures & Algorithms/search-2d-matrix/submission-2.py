class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        mid = 0

        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l, r = 0, len(matrix[m]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if matrix[m][mid] < target:
                        l = mid + 1
                    elif matrix[m][mid] > target:
                        r = mid - 1
                    else:
                        return True
                
                return False
        
        return False

        
                