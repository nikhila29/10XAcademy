const { exec } = require("child_process");
let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');
function readLine() {
  idx++;
  return data[idx - 1];
}
// -------- Do NOT edit anything above this line ----------
let arr = readLine().split(" ").map(Number);
let evensep=[];
let oddsep=[];
for (let i=0;i<arr.length;i++){
    if (arr[i]%2==1){
        evensep.push(arr[i]);
    }
    else{
        oddsep.push(arr[i]);
    }
}

evensep.push(...oddsep);
console.log(evensep.join(" "));