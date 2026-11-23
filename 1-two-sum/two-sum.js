/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const dic = {}
    for(let i=0;i<=nums.length;i++){
        const dif = target - nums[i]
        if(dif in dic){
            return [dic[dif],i]
        }
        dic[nums[i]] = i
    }
};