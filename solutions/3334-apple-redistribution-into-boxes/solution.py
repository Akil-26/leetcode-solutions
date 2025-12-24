class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple = sum(apple)
        capacity.sort(reverse=True)
        i = 0
        while apple > 0:
            apple -= capacity[i]
            i+=1
        return i
