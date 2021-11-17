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
let mini=arr[0]
let maxi=arr[0]
for (let i=0;i<n;i++){
    if (arr[i]<mini){
        mini=arr[i]
    }
    if(arr[i]>maxi){
        maxi=arr[i]
    }
}
console.log(maxi)
console.log(mini)