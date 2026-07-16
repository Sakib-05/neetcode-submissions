from collections import defaultdict
from heapq import *
class Twitter:


    def __init__(self):
        self.time =0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        maxheap.extend(self.tweets[userId])

        for followee in self.followers[userId]:
            if followee == userId: continue
            maxheap.extend(self.tweets[followee])
        
        heapify(maxheap)

        res = []

        while maxheap and len(res) <10:
            res.append(heappop(maxheap)[1])
        
        return res
        


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
