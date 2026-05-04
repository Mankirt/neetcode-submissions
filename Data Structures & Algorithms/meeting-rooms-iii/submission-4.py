class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n

        heap = [] # start time, end time
        for meeting in meetings:
            heapq.heappush(heap, meeting)
        unused_rooms  = [i for i in range(n)] # room number
        used_rooms = [] # [time,number]
        t = 0
        while heap:
            while used_rooms and  t >= used_rooms[0][0]:
                heapq.heappush(unused_rooms,heapq.heappop(used_rooms)[1])
            
            while heap and unused_rooms and heap[0][0] <= t:
                st, end = heapq.heappop(heap)
                room = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, [t + (end - st),room])
                count[room] += 1
            
            if not unused_rooms:
                t = used_rooms[0][0]
            else:
                t += 1





        ans = 0
        for i in range(n):
            if count[i] > count[ans]:
                ans = i
        
        return ans