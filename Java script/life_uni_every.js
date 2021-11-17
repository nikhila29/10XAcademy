let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
while (true){
    let n=parseInt(readLine())
    if (n==42){
        break
    }
    console.log(n) 
}

