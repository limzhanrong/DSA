//same as canSum.js , but returns any array of sum :)
const howSum = (targetSum, numbers, memo = {result:[]}) => {
    if(targetSum === 0){
        return true
    };
    if (targetSum <0){
        return null
    }
    if(targetSum in memo){
        return memo[targetSum]
    }

// Method one passes in memo
    for(let num of numbers){
        if(howSum(targetSum - num, numbers, memo)){
            memo['result'].push(num)
            return memo['result']
        }
    }
    memo[targetSum] = null;
    return null;

}

console.time();
console.log(howSum(7,[2,3,4])); //True
console.log(howSum(11,[5,7,11])); //True
console.log(howSum(7,[5,6])); //False
console.log(howSum(7,[5,3,4,7])); //True
// console.log(howSum(3000, [7,14,3,2,4,5,6])); 
const arr = howSum(3000, [7,14,3,2,4,5,6]);
console.log(arr)
let sum = 0;
arr.forEach((ele)=>{ sum += ele})
console.log(sum)


// console.log(canSum(1501,[5,6])); 


console.timeEnd();