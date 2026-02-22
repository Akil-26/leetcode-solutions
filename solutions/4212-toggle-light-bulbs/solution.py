class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res = []
        for i in range(len(bulbs)):
            if bulbs.count(bulbs[i]) % 2 != 0:
                if bulbs[i] not in res:
                    res.append(bulbs[i])
        return sorted(res)
