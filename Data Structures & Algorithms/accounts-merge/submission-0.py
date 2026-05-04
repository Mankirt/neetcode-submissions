class UnionFind:
    def __init__(self, n ):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
            while self.par[n] != n:
                self.par[n] = self.par[self.par[n]]
                n = self.par[n]
            return n
        
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return 
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf  = UnionFind(len(accounts))
        emailMap = {} # email -> accInd
        for i , acc in enumerate(accounts):
            for email in accounts[i][1:]:
                if email in emailMap:
                    uf.union(i, emailMap[email])
                else:
                    emailMap[email] = i

        accountMap = defaultdict(list)  # AccountInd -> list of emails

        for email, ind in emailMap.items():
            leader = uf.find(ind)
            accountMap[leader].append(email)
        
        res = []
        for ind, email_list in accountMap.items():
            res.append([accounts[ind][0]] + sorted(email_list))
        
        return res











