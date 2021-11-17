let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let str=readLine()
//let p=str.split("").reverse().join("");
//console.log(p)
var splitString = str.split("");
var reverseArray = splitString.reverse();
var joinArray = reverseArray.join("");
if(joinArray==str){
    console.log("True")
}
else{
    console.log("False")
}
//let str = "aaa";
//var splitString = str.split("");
//var reverseArray = splitString.reverse();
//var reverse = reverseArray.join("");
//if (reverse == str) {
//    console.log("True")
//} else {
//    console.log("False")
//}
