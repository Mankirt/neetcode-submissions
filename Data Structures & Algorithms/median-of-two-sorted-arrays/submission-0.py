class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if len(nums1) < len(nums2):
            nums2, nums1 = nums1, nums2
        l = 0
        r = len(nums2)-1
        half = total//2
        while True:
            mid = (r+l)//2
            mid_2 = half-mid-2

            A2 = nums2[mid] if mid>=0 else float('-inf')
            A1 = nums1[mid_2] if mid_2>=0 else float('-inf')

            B2 = nums2[mid+1] if mid+1<len(nums2) else float('inf')
            B1 = nums1[mid_2+1] if mid_2+1<len(nums1) else float('inf')

            if A2<=B1 and A1<=B2:
                if total%2 :
                    return min(B1,B2)
                return (max(A1,A2)+min(B1,B2))/2
            elif A2 > B1:
                r = mid-1
            else :
                l = mid + 1
            
                
                
                    
            
