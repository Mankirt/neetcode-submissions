class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_d=[0]*52
        s_d=[0]*52
        count=0
        for t_a in t:
            t_d[ord(t_a)-ord('a')]+=1
        l=0
        r=0
        res=(len(s)+1,0,len(s))
        while r<len(s):
            ind=ord(s[r])-ord('a')
            s_d[ind]+=1
            if t_d[ind]:
                if s_d[ind]<=t_d[ind]:
                    
                    count+=1
            while count==len(t) and l<=r:
                print(l,r)
                if res[0]>r-l+1:
                    res=(r-l+1,l,r+1)
                    
                ind2=ord(s[l])-ord('a')
                s_d[ind2]-=1
                
                if t_d[ind2]:
                    if s_d[ind2]<t_d[ind2]:
                        count-=1
                l+=1
            r+=1
        return s[res[1]:res[2]] if res[0]<len(s)+1 else ""
