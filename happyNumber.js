var isHappy = function(n,memo={}) {
    if(n===1) return true
    if(n in memo) return false
    let nString = n.toString()
    let sum = 0
    for(let i = 0; i < nString.length; i++){
        sum += Math.pow(Number(nString.charAt(i)),2)
    }
    memo[n] = sum
    return isHappy(sum, memo)
};

isHappy(2)