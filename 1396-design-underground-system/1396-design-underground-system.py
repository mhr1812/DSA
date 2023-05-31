class UndergroundSystem:

    def __init__(self):
        self.m = {}
        self.avg = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.m[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.m[id]
        x = t - startTime
        self.avg[(startStation, stationName)].append(x)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.avg[(startStation, endStation)]
        return sum(times) / len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)