class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findSum(k, arr, tar, crr):
            if k == 2:
                left = 0
                right = len(arr) - 1
                while left < right:
                    if arr[left] + arr[right] == tar:
                        
                        res.append(crr + [arr[left], arr[right]])
                        
                        left+=1
                        right-=1

                        while left < len(arr) and arr[left] == arr[left-1]:
                            left += 1
                    elif arr[left] + arr[right] < tar:
                        left += 1
                    
                    else:
                        right -= 1
                return
            
            for i in range(len(arr)):
                if i>0 and arr[i] == arr[i-1]:
                    continue
                crr.append(arr[i])
                findSum(k-1, arr[i+1:], tar - arr[i], crr)    
                crr.pop()
        
        nums.sort()
        res = []
        findSum(4, nums, target, [])
        return res