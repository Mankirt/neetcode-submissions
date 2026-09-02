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
                if counter[i] == 0:
                    return False
                counter[i] -= 1
                while heap and counter[heap[0]] == 0:
                    heapq.heappop(heap)
        return True

        