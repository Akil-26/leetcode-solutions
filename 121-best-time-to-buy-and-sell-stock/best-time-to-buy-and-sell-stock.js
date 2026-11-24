/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxp = 0;
    let minbuy = prices[0];
    for(let sell of prices){
        maxp = Math.max(maxp,sell - minbuy)
        minbuy = Math.min(minbuy,sell)
    }
    return maxp
}