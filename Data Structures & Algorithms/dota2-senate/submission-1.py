class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        win = 0
        q = deque(list(senate))
        while count["R"] > 0 and count['D'] > 0:
            node = q.popleft()
            if node == 'R':
                win += 1
                if win > 0:
                    q.append('R')
                else:
                    count["R"] -= 1
            else:
                win -= 1
                if win < 0:
                    q.append('D') 
                else:
                    count["D"] -= 1


        return 'Radiant' if count['R'] else 'Dire'