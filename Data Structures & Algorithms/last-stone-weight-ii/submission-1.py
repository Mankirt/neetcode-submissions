class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_s = sum(stones)
        target = math.ceil(sum_s/2)

        dp = {0}

        for st in stones:
            temp = set()
            for v in dp:
                if v+st == target:
                    return target*2 - sum_s
                elif v+st<target:
                    temp.add(v+st)
                temp.add(v)
            dp = temp
        return sum_s-max(dp)*2 