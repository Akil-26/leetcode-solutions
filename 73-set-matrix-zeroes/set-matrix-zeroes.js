/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const rowSet = new Set();
    const colSet = new Set();
    const row = matrix.length
    const col = matrix[0].length
    for (let i = 0; i<row; i++){
        for (let j=0; j<col; j++){
            if (matrix[i][j] == 0){
                rowSet.add(i)
                colSet.add(j)
            }
        }
    }
    for (let i = 0; i<row; i++){
        for (let j=0; j<col; j++){
            if (rowSet.has(i) || colSet.has(j)){
                matrix[i][j] = 0
            }
        }
    }
};