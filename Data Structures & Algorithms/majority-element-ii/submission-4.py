class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if len(count) > 2:
                new_count = defaultdict(int)
                for key in count:
                    if count[key] > 1:
                        new_count[key] = count[key] - 1
                count = new_count
        ans = []
        for num in count:
            if nums.count(num) > len(nums)//3:
                ans.append(num)
        
        return ans