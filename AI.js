var state = require('./megaTTT.js');
var first = state([],[]);

function rate_move(move, depth) {        
    var moves = move.valid_moves();
    if(depth===0) {
        var ratings = [];
        for(i in moves) {
            ratings[i] = moves[i].score();
        };
        return rate(ratings);
    } else {
        var ratings = [];
        for(i in moves) {
            ratings[i] = rate_move(moves[i], depth-1);
        };
        return rate(ratings);
    };
};

function rate(array) {
    return -Math.max.apply(null, array);
};

module.exports = rate_move;
