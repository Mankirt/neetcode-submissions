class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        l = 1
        r = mountainArr.length() - 2
        while l <= r:
            m = l + (r-l)//2
            if mountainArr.get(m-1) < mountainArr.get(m) > mountainArr.get(m + 1):
                break
            elif mountainArr.get(m-1) > mountainArr.get(m) > mountainArr.get(m + 1):
                r = m - 1
            else :
                l = m + 1
        
        #Check in left:
        l = 0
        r = m - 1
        while l <= r:
            mid = l + (r-l)//2
            if  mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1
        
        l = m
        r = mountainArr.length() - 1
        while l <= r:
            mid = l + (r-l)//2
            if  mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
