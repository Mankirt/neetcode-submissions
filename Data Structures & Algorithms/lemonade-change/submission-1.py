class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0,10:0,20:0}

        for bill in bills:
            if bill == 20:
                if d[10]>0:
                    d[10]-=1
                    if d[5]>0:
                        d[5]-=1
                    else:
                        return False
                elif d[5]>=3:
                    d[5] -=3
                else:
                    return False
            elif bill == 10:
                if d[5]>0:
                    d[5]-=1
                else:
                    return False
            
            d[bill] +=1
        
        return True
                