//Write a function canSum(targetSum, numbers) that takes in a 
//targetSum and an array of numbers as arguments.

//The function should return a boolean indicating whether or not it
//is possible to generate the targetSum using numbers from the array.

//You may use an element of the array as many times as needed.
//You may assume that all input numbers are non-negative;

const canSum = (targetSum, numbers,memo={}) =>{
    if(targetSum in memo) return memo[targetSum];
    if(targetSum === 0) return true;
    if(targetSum < 0) return false;
    // Loops through numbers array
    for(let i = 0; i< numbers.length; i++){
        if (canSum(targetSum - numbers[i], numbers, memo) === true) {
            // memo[targetSum] = true;
            return true;
        }
    }
    memo[targetSum] = false;
    return false;
}

console.time();
console.log(canSum(7,[2,3,4])); //True
console.log(canSum(11,[5,7,11])); //True
console.log(canSum(7,[5,6])); //False
console.log(canSum(7,[5,3,4,7])); //True
console.log(canSum(300, [7,14])); //

// console.log(canSum(1501,[5,6])); 


console.timeEnd();