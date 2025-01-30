class Solution {
    public void rotate(int[] nums, int k) {
        //[1234567] ->   [7123456] -> [5671234]
        // 1234567
          //  s e 7234561 ->7634521 ->7654321
        //first -> reverse -> [7654321]

        //second - 0 to k-1 revrse ->[5674321]

        // third -> k to nums.length -1 ->[5674321]
     k = k%nums.length;
   reverse(nums,0,nums.length-1);
    reverse(nums,0,k-1);
    reverse(nums,k,nums.length-1);

        
    }
    public void reverse(int  []nums,int start,int end){

        while(start <= end){
            int temp = nums[start];
            nums[start]= nums[end];
            nums[end]= temp;
            start ++;
            end --;


        }

    }
}
