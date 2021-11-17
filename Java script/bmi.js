let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----
//BMI = (weight) / (height * height)
let heightInCm=parseInt(readLine())
let weightInKg=parseInt(readLine())
let heightInMeters= heightInCm/100
let name=readLine()
let bmi=(weight)/(heightInMeters*heightInMeters)
if(bmi>=25){
    console.log(`Hey ${name} you are overweight`)
}
else if(bmi<18){
    console.log(`Hey ${name} you are underweight`)
}
else{
    console.log(`Hey ${name} you are having normal weight`)
}
