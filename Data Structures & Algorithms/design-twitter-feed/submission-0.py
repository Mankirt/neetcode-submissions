class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if len(self.tweetMap[followee])>0:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][index]
                minHeap.append([count,tweetId,followee,index-1])
        heapq.heapify(minHeap)

        while minHeap and len(res)<10:
            count,tweetId,followee,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap,[count,tweetId,followee,index-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
