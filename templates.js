
// Binary Search -> First Bad Version.
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        var firstPointer = 1, lastPointer = n;
        while(firstPointer < lastPointer){
            var middle = Math.floor(firstPointer + (lastPointer - firstPointer)/2);
            if(!isBadVersion(middle)){
                firstPointer = middle + 1;
            }else{
                lastPointer = middle;
            }
        }
        return firstPointer;
    };
};