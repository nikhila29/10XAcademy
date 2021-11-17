let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

function addlist(lst1,lst2){
    lst4=[];
    i=0;
    if(lst1.length>lst2.length){
        main1=lst1.length-lst2.length;
        zero=new Array(main1).fill(0);
        list2.push(...zero);
    }
    else{
        main1=lst2.length-lst1.length;
        zero=new Array(main1).fill(0);
        list1.push(...zero);
    }
    b=0;
    for(i=0;i<lst1.length;i++){
        num=parseInt(lst1[i])+parseInt(lst2[i])+parseInt(b);
        b=parseInt(num/10);
        res=num%10;
        lst4.push(res);
    }
    if(b>0){
        lst4.push(b);
    }
    return lst4.join("");
}
testno=parseInt(readLine());
for(j=0;j<testno;j++){
    list1=readLine().split(" ").map(Number);
    list2=readLine().split(" ").map(Number);
    console.log(addlist(list1,list2))
}