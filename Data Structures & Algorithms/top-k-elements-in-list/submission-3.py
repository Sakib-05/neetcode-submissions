class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hp=defaultdict(int)

        frequency = [[] for i in range(0,len(nums)+1)]
        #index is the frequency and the list at that index is the values that occur 'i' times

        for num in nums:
            hp[num] +=1

        for num, count in hp.items():
            frequency[count].append(num)

        res =[]

        while len(res) < k:
            res += frequency.pop()

        return res

        