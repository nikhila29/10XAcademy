let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----
let Name=[];
let favoriteMovies=[];
function addFavoriteMovie(moviename){
    favoriteMovies.push(moviename);
}
function printFavoriteMovies(){
    for(i=0;i<favoriteMovies.length;i++){
        console.log(favoriteMovies[i])
    }
}

addFavoriteMovie('surya')
addFavoriteMovie('winner')
addFavoriteMovie('leader')
printFavoriteMovies()

