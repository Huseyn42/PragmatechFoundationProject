//1.
var total = 0, i = 1;
while (i <= 100) {
    total += i;
    i += 1;
}
console.log (total);

//2.


//3.
let arr=[1,3,4,6,89,12,67,34,89,123]
console.log (arr [9])

let result = arr.reduce((sum, current) => sum + current);
console.log (result)



let odds = arr.filter (a => a%2)
console.log (odds)

