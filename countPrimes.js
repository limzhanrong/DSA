/**
 * @param {number} n
 * @return {number}
 */
 var countPrimes = function(n) {
    //     Brute Force Approach
        // let primes = []
        // loop: for(let i = 0; i <n; i++){
        //     if((i%2===0 && i !== 2) || i === 1){
        //         continue;
        //     }
        //     let squareRoot = Math.sqrt(i);
        //     for(let num of primes){
        //         if (num > squareRoot) break;
        //         if (i % num === 0) continue loop;
        //     }
        //     primes.push(i);
        // }
        // return primes.length
    // Optimal Approach (Sieve of Eratosthenes)
        let count = 0
        let primes = new Array(n+1).fill(true)
    //     0, 1, 2, 3, 4, 5, 6, 7, 8
    //      t, t, t, t, t, t, t, t, t
    //     Loops from 2 until the end.
        for(let i = 2; i < n; i++){
            if(primes[i] === true){
                count++;
                for(let j = i * i;  j <= n; j+=i){
                    primes[j] = false
                }
            }
        }
        return count;
    };