class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1)
        
        left_size = ((len(nums1)+len(nums2))+1)//2
        med = 0
        while left <= right:
            mid1 = (left+right)//2
            mid2 = left_size - mid1

            l1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < len(nums1) else float('inf')

            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                total = len(nums1) + len(nums2)
                if total % 2 != 0:
                    return float(max(l1,l2))
                else:
                    return float((max(l1,l2) + min(r1,r2))/2)
            elif l1 > r2:
                right = mid1-1
            else: 
                left = mid1 + 1

        
sol = Solution()
nums1 = [1,3]
nums2 = [2,4]
print(sol.findMedianSortedArrays(nums1,nums2))
        