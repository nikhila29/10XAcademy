let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// -------- Do NOT edit anything above this line ----------

function difference_of_sum_of_even_odd(list1){
    let evensum=0;
    let oddsum=0;
    for(i=0;i<list1.length;i++){
        if(i%2==1){
            evensum=evensum+list1[i]
        }
        else{
            oddsum=oddsum+list1[i]
        }
    }
    final=oddsum-evensum
    console.log(final)
}

list1=readLine().split(" ").map(Number)
difference_of_sum_of_even_odd(list1)