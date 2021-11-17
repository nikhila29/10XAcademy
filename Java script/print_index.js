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
    arr.push(readLine())
}
for(let i=0;i<n;i++){
    console.log((i),arr[i])   
}