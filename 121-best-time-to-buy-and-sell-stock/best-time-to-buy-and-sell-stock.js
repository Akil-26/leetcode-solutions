/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let left = 0;
    let right = 1;
    let maxp = 0;

    while(right<prices.length){
        if (prices[right]<prices[left]){
            left = right;
        }else{
            maxp = Math.max(maxp,prices[right]-prices[left])
        }
        right++
    }
    return maxp
};