/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    res = 0;
    left = 0;
    right = height.length - 1;

    leftmax = height[left];
    rightmax = height[right];

    while(left < right){
        if(leftmax < rightmax){
            left+=1;
            leftmax = Math.max(leftmax,height[left]);
            res += leftmax - height[left];
        }
        else{
            right-=1;
            rightmax = Math.max(rightmax,height[right]);
            res += rightmax - height[right];
        }
    }
    return res
};