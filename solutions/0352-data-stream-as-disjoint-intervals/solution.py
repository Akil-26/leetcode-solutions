class SummaryRanges:

    def __init__(self):
        self.array = []
    def addNum(self, value: int) -> None:
        if value not in self.array:
            self.array.append(value)
        self.array.sort()
    def getIntervals(self) -> List[List[int]]:
        ans = []
        i = 0
        while i <len(self.array):
            start = self.array[i]
            while i+1 < len(self.array) and self.array[i+1] == self.array[i]+1:
                i+=1
            if start == self.array[i]:
                ans.append([start,self.array[i]])
            else:
                ans.append([start,self.array[i]])
            i+=1
        return ans
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
