let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let l=parseInt(readLine())
let b=parseInt(readLine())
if (l<=0) 
{
    console.log(0)	
}
else if(b<=0){
    console.log(0)
}
else{
    console.log(parseInt(2*(l+b)))
}

