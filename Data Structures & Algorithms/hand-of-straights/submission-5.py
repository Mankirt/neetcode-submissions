class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        heap = []
        for key in counter:
            heapq.heappush(heap, key)

        while heap:
            crr = heap[0]
            for i in range(crr,crr+groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
