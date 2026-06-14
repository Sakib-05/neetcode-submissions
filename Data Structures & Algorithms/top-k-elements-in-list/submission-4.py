class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for x in range(len(nums)+1)]

        hp= defaultdict(int)

        for num in nums:
            hp[num]+=1
        
        for num,count in hp.items():
            bucket[count].append(num)
        
        res=[]

        while len(res) < k:
            res+=bucket.pop()
        
        return res
        