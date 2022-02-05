// Slowest Fib Function, 2^n complexity.

const fib_1 = (n) => {
    if(n <= 2){
        return 1;
    }
    return fib_1(n-1) + fib_1(n-2);
}

// Memoization.
// JS object, keys will be argument (Which is n in this case) of the function, value will be the return value
// fib_2 has a time complexity of O(2N), which would be O(N). Draw out the tree to visualize.
const fib_2 = (n, memo={}) => {
    //If Memo already exists, returns the value.
    if(n in memo){
        return memo[n];
    }
    if(n <= 2){
        return 1;
    }
    //If Memo doesn't exist, store a new memo.
    memo[n] = fib_2(n-1, memo) + fib_2(n-2,memo);
    console.log(memo[n]);
    return memo[n];
}

console.log(fib_1(5));
console.log(fib_2(20));

