let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');
function readLine() {
  idx++;
  return data[idx - 1];
}
// -------- Do NOT edit anything above this line ----------
//S = "ABCDE"
// mx = 1 // a
// mx = max(mx, len(bb)) // bb
// mx = max(mx, len(ccc) = 3
/**let str = readLine();
let count = 0;
// O(n)
for(let left=0, right; left<str.length; left = right) {
	right = left;
	
	while(right<str.length && str[left]==str[right]) {
		right += 1;
	}
	
	let curLen = right - left;
	
	count= Math.max(count, curLen);
}
console.log(count);**/
let str=readLine();
let count=0
let power=0
for (let i=0;i<str.length;i++){
    if (str[i]===str[i-1]){
        count+=1
    }
    else{
        power=Math.max(power,count)
        count=1
    }
power=Math.max(power,count)
}
console.log(power)
