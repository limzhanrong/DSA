
//set nth bit as one
function set_nth_bit(m,n){
    console.log('original number:' + '\n' + m.toString(2))
    m=m|1<<n
    console.log('after number:' + '\n' + m.toString(2))
    return m
}

console.log(set_nth_bit(0,3))