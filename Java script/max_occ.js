let fs = require("fs");
const { maxHeaderSize } = require("http");
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
arr.sort()
if (n===0){
    console.log(-1)
}
else{
    let count=1
    let maxm=1
    for (let i=0;i<arr.length-1;i++){
        if(arr[i]===arr[i+1]){
            count+=1
            maxm=Math.max(maxm,count)
            continue
        }
        count=1
    }
   
   console.log(maxm)

}