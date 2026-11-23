/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b)=>a-b);
    const res = [];
    const n = nums.length;

    for([i,num] of nums.entries()){
        if (i>0 && num == nums[i-1]){
            continue
        } 

        left = i+1
        right = n-1

        while(left < right){
            s = num + nums[left] + nums[right]
            if (s<0){
                left ++
            }
            else if (s>0){
                right--
            }
            else{
                res.push([num,nums[left],nums[right]]);
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