let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n = readLine();
let arr = [];
while(n){
    arr.push(parseInt(readLine()));
    n -= 1;
}
arr.reverse()
for(let i in arr){
  console.log(arr[i])
}


