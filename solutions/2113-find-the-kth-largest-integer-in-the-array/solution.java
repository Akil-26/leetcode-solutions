class Solution {
    public String kthLargestNumber(String[] nums, int k) {
         Arrays.sort(nums, (a, b) -> {
            // Compare by length
            if (a.length() != b.length()) {
                return Integer.compare(a.length(), b.length());
            }
            // If same length, compare lexicographically
            return a.compareTo(b);
        });
        
        // kth largest = size - k
        return nums[nums.length - k];
    }
}
