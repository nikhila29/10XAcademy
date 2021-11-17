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
let max_limit=parseInt(readLine())
let m=parseInt(readLine())
let arr=new Array(n).fill(0)
let res=0
for (let i=0;i<m;i++){
    let dial=parseInt(readLine())
    arr[dial-1]+=1
    if(arr[dial-1]===max_limit){
        res=dial
        break
    }

    
}
console.log(res)
