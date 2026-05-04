class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l=[0]*26
        for task in tasks:
            l[ord(task)-ord('A')]+=1
        
        l.sort()
        m=l[-1]
        extra_space = (m-1)* n
        for i in range(len(l)-2,-1,-1):
            if l[i]==m:
                extra_space-=m-1
            else:
                extra_space-=l[i]
        return len(tasks)+extra_space if extra_space>0 else len(tasks)
