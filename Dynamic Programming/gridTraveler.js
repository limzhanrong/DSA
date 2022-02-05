
const gridTraveler = (m, n, memo = {}) => {
    const key = m + "," + n;
    const flipped_key = n + ',' + m;
    //Checks if Args in the memo.
    if(memo[key]){
        return memo[key];
    }
    if(memo[flipped_key]){
        return memo[flipped_key];
    }
    if (m === 1 && n === 1) return 1;
    if (m === 0 || n === 0) return 0;
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo);
    return memo[key];
}

// m * n complexity.

console.log(gridTraveler(18, 18));