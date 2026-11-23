/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b)=>a-b);
    const res = [];
    const n = nums.length;

    for(i=0; i <= n; i++){
        if (i>0 && nums[i] == nums[i-1]){
            continue
        } 
        
        left = i+1
        right = n-1

        while(left < right){
            s = nums[i] + nums[left] + nums[right]
            if (s<0){
                left ++
            }
            else if (s>0){
                right--
            }
            else{
                res.push([nums[i],nums[left],nums[right]]);
                left++
                right--
                while(left < right && nums[left] == nums[left-1]){
                    left++
                }
            }
        }
    }
    return res
};