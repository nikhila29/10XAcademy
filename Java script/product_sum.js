let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n=readLine()
let num=n.toString()
let sum=0
let product=1
for(let i of num){
	sum+=parseInt(i)
	product*=parseInt(i)
	pro_sum=product-sum
}
console.log(pro_sum)
