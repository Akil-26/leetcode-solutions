class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = []
        res = []
        left = right = 0
        while right < len(nums):
            while que and nums[que[-1]] < nums[right]:
                que.pop()
            que.append(right)
            if left > que[0]:
                que.pop(0)
            if (right + 1) >= k:
                res.append(nums[que[0]])
                left += 1
            right += 1
        return res