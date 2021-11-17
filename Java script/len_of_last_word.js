let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let str= readLine()
//var word = str.split("-").pop();
//var lastIndex = str.lastIndexOf(" ");
//word= str.substring(0, lastIndex);
//var mySplitResult = str.split(" ");
//var lastWord =  mySplitResult[mySplitResult.length-1]
let words=str.split(" ");
let lastWord=words[words.length-1]
console.log(lastWord.length)