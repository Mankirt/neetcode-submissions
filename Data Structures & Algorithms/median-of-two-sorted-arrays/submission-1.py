class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        l = 0 
        r = len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total//2
        while True:
            nums1_ind = l + (r-l)//2
            nums2_ind = half - nums1_ind - 2
            nums1Left = nums1[nums1_ind] if nums1_ind >=0 else float('-inf')
            nums1Right = nums1[nums1_ind + 1] if nums1_ind + 1 < len(nums1) else float('inf')
            nums2Left = nums2[nums2_ind] if nums2_ind >=0 else float('-inf')
            nums2Right = nums2[nums2_ind + 1] if nums2_ind + 1 < len(nums2) else float('inf')

            if nums1Left > nums2Right:
                r = nums1_ind - 1
            elif nums2Left > nums1Right:
                l = nums1_ind + 1
            else:
                if total%2:
                    return min(nums1Right,nums2Right)
                return (max(nums1Left, nums2Left) + min(nums1Right,nums2Right))/2

