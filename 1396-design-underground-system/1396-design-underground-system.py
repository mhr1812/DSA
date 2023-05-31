class UndergroundSystem:

    def __init__(self):
        self.journey = defaultdict(set)
        self.history = defaultdict(set)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.journey[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.journey.pop(id)
        x = (startStation, stationName)
        allTime, allCount = self.history.get(x,(0,0))
        self.history[x] = (allTime+t-startTime,allCount+1)
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x = (startStation,endStation)
        allTime, allCount = self.history.get(x,(0,0))
        return allTime/allCount
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)