class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = list()
        self.store[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
                    return ""
        
        res = ""
        left = 0
        right = len(self.store[key])-1
        while left <= right:
            mid = (left+right)//2
            if self.store[key][mid][0] > timestamp:
                right = mid-1
            else:
                res = self.store[key][mid][1]
                left = mid+1
        return res
timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
print(timeMap.get("alice", 1))         
print(timeMap.get("alice", 2))      
timeMap.set("alice", "sad", 3)   
print(timeMap.get("alice", 3))          