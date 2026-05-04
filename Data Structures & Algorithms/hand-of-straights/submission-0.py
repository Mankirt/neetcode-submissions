class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        c = {}

        for num in hand:
            c[num] = 1 + c.get(num,0)

        q = list(c.keys())
        heapq.heapify(q)

        while q:
            first = q[0]

            for i in range(first,first+groupSize):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    if i!=q[0]:
                        return False
                    heapq.heappop(q)
        return True
