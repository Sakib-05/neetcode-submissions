class TimeMap:

    def __init__(self):
        self.hp=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hp[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        last_val=""
        l=0
        r=len(self.hp[key])-1
        while l<=r:
            k=(l+r)//2
            if self.hp[key][k][0]<=timestamp:
                last_val=self.hp[key][k][1]
                l=k+1
            else:
                r=k-1


        return last_val
        
