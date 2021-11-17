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
for (let i=0;i<n;i++){
    arr.push(parseInt(readLine()))
}
let odd_count=0,even_count=0
for (let num of arr){
    if(num%2==0){
        even_count+=1
    }
    if(num%2!=0){
        odd_count+=1
    }
}
console.log(odd_count)
console.log(even_count)
