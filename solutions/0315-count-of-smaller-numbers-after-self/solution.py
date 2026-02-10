class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0]*n
        enum = list(enumerate(nums))
        def merge(li):
            if len(li) <= 1:
                return li
            mid = len(li) // 2
            left = merge(li[:mid])
            right = merge(li[mid:])

            merged = []
            i = j = 0
            right_count = 0
            
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    count[left[i][0]] += right_count
                    merged.append(left[i])
                    i+=1
                else:
                    right_count += 1
                    merged.append(right[j])
                    j+=1
            
            while i < len(left):
                count[left[i][0]] += right_count
                merged.append(left[i])
                i+=1
            
            while j < len(right):
                merged.append(right[j])
                j+=1

            return merged
            
        merge(enum)
        return count
