class TimeMap:

    def __init__(self):
        self.hp=dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp= self.hp.get(key,{})
        temp[timestamp] = value
        self.hp[key]= temp
        

    def get(self, key: str, timestamp: int) -> str:
        timestamps=list(self.hp.get(key,{}).keys())
        recent_time=0
        l=0
        r=len(timestamps)-1
        while l<=r:
            k=(l+r)//2
            if timestamps[k]<=timestamp:
                recent_time=timestamps[k]
                l=k+1
            else:
                r=k-1


        return self.hp.get(key,{}).get(recent_time,"")
        
