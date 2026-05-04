class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        heap = []
        for key in c:
            heapq.heappush(heap,key)

        while heap:
            first = heap[0]

            for i in range(first,first+groupSize):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
            
        return True
