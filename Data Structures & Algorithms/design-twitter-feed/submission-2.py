class Twitter:

    def __init__(self):
        self.followd = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time,tweetId])
        self.time+=1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        total_tweets = deepcopy(self.userTweets[userId])
        for user in self.followd[userId]:
            total_tweets.extend(self.userTweets[user])
        heap  = total_tweets
        heapq.heapify(heap)
        while len(heap)>10:
            heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followd[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followd[followerId]:
            self.followd[followerId].remove(followeeId)
        return
