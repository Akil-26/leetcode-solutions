class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # c = 1
        # v = 1
        # while c < k:
        #     if v in arr:
        #         v+=1
        #     else:
        #         v+=1
        #         c+=1
        # return v
        left,right = 0,len(arr)-1
        while left<=right:
            mid = (left+right) // 2
            missing = arr[mid] - (mid+1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k