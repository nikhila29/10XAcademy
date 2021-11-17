let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var str=readLine().split(' ')
var longestWord=0
for (let i=0;i<str.length;i++){
    if(str[i].length>longestWord){
        longestWord=str[i].length
    }
    
}
console.log(longestWord)
