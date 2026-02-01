from collections import deque

class RideSharingSystem:
    def __init__(self):
        self.waiting_riders = deque()
        self.available_drivers = deque()
        self.active_riders = set()
        self.rimovexalu = []

    def addRider(self, riderId: int) -> None:
        if riderId not in self.active_riders:
            self.waiting_riders.append(riderId)
            self.active_riders.add(riderId)
            self.rimovexalu = list(self.waiting_riders)

    def addDriver(self, driverId: int) -> None:
        self.available_drivers.append(driverId)

    def matchDriverWithRider(self) -> list[int]:
        if not self.waiting_riders or not self.available_drivers:
            return [-1, -1]
        
        driver = self.available_drivers.popleft()
        rider = self.waiting_riders.popleft()
        
        self.active_riders.remove(rider)
        
        self.rimovexalu = list(self.waiting_riders)
        
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.active_riders:
            self.waiting_riders.remove(riderId)
            self.active_riders.remove(riderId)
            self.rimovexalu = list(self.waiting_riders)
