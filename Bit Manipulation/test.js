// Get Nth Bit from right
function get_nth(m,n) {
    mask = 1<<n
    console.log('original number:' + '\n' + m.toString(2))
    console.log('mask:' + '\n' + mask.toString(2))

    if(m&mask){
        return true
    }
    return false
}
// Set Nth Bit from right using logic OR

// Set Nth Bit from right
console.log(get_nth(5,2))
// console.log(~2323)