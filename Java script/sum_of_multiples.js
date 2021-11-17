let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n=parseInt(readLine())
let arr=[]
for(let i=0;i<n;i++){
    arr.push(parseInt(readLine()))
}
let i=parseInt(readLine())
let sum=0
for (let num of arr){
    if (num%i===0){
        sum+=num
    }

}
console.log(sum)