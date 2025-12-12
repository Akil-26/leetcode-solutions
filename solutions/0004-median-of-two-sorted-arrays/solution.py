class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s= sorted(nums1+nums2)
        print(s)
        if len(s) % 2 != 1:
            n1 = s[(len(s) // 2)-1]
            n2 =  s[(len(s) // 2)]
            return (n1+n2)/2
        else:
            return s[len(s)//2]
