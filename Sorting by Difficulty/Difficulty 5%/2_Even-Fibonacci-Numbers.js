function sumEvenFibonacci(limit) {
    let a = 1, b = 2;
    let sum = 0;

    while (b <= limit) {
        if (b % 2 === 0) {
            sum += b;
        }
        let temp = a + b;
        a = b;
        b = temp;
    }

    return sum;
}

console.log(sumEvenFibonacci(4000000));

//4613732