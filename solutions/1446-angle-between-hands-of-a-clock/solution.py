class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = 6.0 * minutes
        h = 30.0 * (hour%12) + 0.5 * minutes
        angle = abs(h-m)
        return min(angle,360.0-angle)
