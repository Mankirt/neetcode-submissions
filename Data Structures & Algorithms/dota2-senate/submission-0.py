class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d = 0,0
        for s in senate:
            if s=='R':
                r+=1
            else:
                d+=1
        
        m = 0

        senate = list(senate)

        while senate and r>0 and d>0:
            s = senate.pop(0)
            if s == 'R':
                if m<=0:
                    senate.append(s)
                    d-=1
                m-=1
            else:
                if m>=0:
                    senate.append(s)
                    r-=1
                m+=1
        
        return "Radiant" if r>0 else "Dire"