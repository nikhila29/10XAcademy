let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let p=parseInt(readLine())
let q=parseInt(readLine())
let r=parseInt(readLine())
console.log((p*q*r)/100) 
