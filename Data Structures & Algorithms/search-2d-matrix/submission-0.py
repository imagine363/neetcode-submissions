class Solution:
    def searchMatrix(self, matrix, target):
        top = 0
        bottom = len(matrix)-1
        while top <= bottom:
            midr = (top+bottom)//2
            if matrix[midr][-1] < target:
                top = midr+1
            elif matrix[midr][0] > target:
                bottom = midr - 1
            else:
                arr = matrix[midr]
                left = 0
                right = len(arr)-1
                while left <= right:
                    midc = (left+right)//2
                    if arr[midc] < target:
                        left = midc+ 1
                    elif arr[midc] > target:
                        right = midc-1
                    else:
                        return True
                return False
        return False
sol = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
target = 15

print(sol.searchMatrix(matrix,target))

        