let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
/*let n=parseInt(readLine())
if (n<0){
    n=n*-1
    num=n.toString()
    num.split("").reverse().join("");
    let rev=parseInt(num)
    console.log(-1*rev)
}
else{
    num=n.toString()
    num.split("").reverse().join("");
    let rev=parseInt(num)
    console.log(rev)
}
*/
/*let neg=false
if (n<0){
    n*=(-1)
    let neg=true
}
n.toString()
n.split(" ")
n.reverse()
n.join("");
n=parseInt(n)
if (neg===true){
    n*=(-1)
}
console.log(n)*/



let n=parseInt(readLine())
let neg=(n<0)
n=Math.abs(n)
/*if(n<0){
    n*=-1
    let neg=true
}*/
let sum=0
while (n>0){
    digit=n%10
    sum=sum*10+digit
    n=Math.floor(n/10)
}
if (neg===true){
    sum=-sum
}
console.log(sum)


