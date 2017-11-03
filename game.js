var state = require('./megaTTT.js');
var best_move = require('./AI.js');

process.stdin.resume();
process.stdin.setEncoding('utf8');

var first = state([],[]);

console.log(first.print());
console.log(first.valid_moves().map(i=>i.data[i.data.length-1][1]));
move();
function move() {
    process.stdin.on('data', function (chunk) {
        first = first.valid_moves()[Number(chunk)];
        var valid_moves = first.valid_moves();
        var moves = [];
        for(i in valid_moves) {
            moves.push(best_move(valid_moves[i], 3));
        };
        first = valid_moves[moves.indexOf(Math.max.apply(null, moves))];
        console.log(first.print());
        //console.log(first.update_win());
        console.log(first.valid_moves().map(i=>i.data[i.data.length-1][1]));
    });
};
