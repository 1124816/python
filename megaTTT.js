var state = {
    data: [],
    dataL: [[],[],[],[],[],[],[],[],[],],
    wins: [],
    has_won: undefined, 

    print() {
        var s = [[ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ],[ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ],[ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ],[ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ], [ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ], [ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ], [ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ], [ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ], [ ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ['   '], ]];

        for(i in this.data) {
            s[this.data[i][1][0]][this.data[i][1][1]][0] = ` ${this.data[i][0]} `;
        };

        console.log(`${s[0][0]} | ${s[0][1]} | ${s[0][2]} || ${s[1][0]} | ${s[1][1]} | ${s[1][2]} || ${s[2][0]} | ${s[2][1]} | ${s[2][2]}
${s[0][3]} | ${s[0][4]} | ${s[0][5]} || ${s[1][3]} | ${s[1][4]} | ${s[1][5]} || ${s[2][3]} | ${s[2][4]} | ${s[2][5]}
${s[0][6]} | ${s[0][7]} | ${s[0][8]} || ${s[1][6]} | ${s[1][7]} | ${s[1][8]} || ${s[2][6]} | ${s[2][7]} | ${s[2][8]}
${s[3][0]} | ${s[3][1]} | ${s[3][2]} || ${s[4][0]} | ${s[4][1]} | ${s[4][2]} || ${s[5][0]} | ${s[5][1]} | ${s[5][2]}
${s[3][3]} | ${s[3][4]} | ${s[3][5]} || ${s[4][3]} | ${s[4][4]} | ${s[4][5]} || ${s[5][3]} | ${s[5][4]} | ${s[5][5]}
${s[3][6]} | ${s[3][7]} | ${s[3][8]} || ${s[4][6]} | ${s[4][7]} | ${s[4][8]} || ${s[5][6]} | ${s[5][7]} | ${s[5][8]}
${s[6][0]} | ${s[6][1]} | ${s[6][2]} || ${s[7][0]} | ${s[7][1]} | ${s[7][2]} || ${s[8][0]} | ${s[8][1]} | ${s[8][2]}
${s[6][3]} | ${s[6][4]} | ${s[6][5]} || ${s[7][3]} | ${s[7][4]} | ${s[7][5]} || ${s[8][3]} | ${s[8][4]} | ${s[8][5]}
${s[6][6]} | ${s[6][7]} | ${s[6][8]} || ${s[7][6]} | ${s[7][7]} | ${s[7][8]} || ${s[8][6]} | ${s[8][7]} | ${s[8][8]}`);
    },

    valid_moves() {
        if(this.data.length===0) {
            var returner = [];
            var x = 0;
            while(x<9) {
                var newdata = this.data.slice();
                newdata.splice(newdata.length, 0, ['x',[4,x]]);
                returner.push(state_factory(newdata, this.wins.slice()));
                x++;
            };
            return returner;
        } else {
            var last_play = this.data[this.data.length-1][0];
            var returner = [];
            var next = this.data[this.data.length-1][1][1];
            var x = 0;
            var wins = this.update_win();
            if(wins[next]===undefined) {
                while(x<9) {
                    if(this.dataL[next][x]===undefined) {
                        var newdata = this.data.slice();
                        newdata.splice(newdata.length, 0, [(last_play==='x'?'y':'x'),[next,x]]);
                        returner.push(state_factory(newdata, this.wins.slice()));
                    };
                    x++;
                };
                if(returner.length===0) {
                    var x = 0;
                    while(x<9) {
                        var y = 0;
                        while(y<9) {
                            if(this.dataL[x][y]===undefined) {
                                var newdata = this.data.slice();
                                newdata.splice(newdata.length, 0, [(last_play==='x'?'y':'x'),[x,y]]);
                                returner.push(state_factory(newdata, this.wins.slice()));

                            };
                            y++;
                        };
                        x++;
                    };
                };
            } else {
                var x = 0;
                while(x<9) {
                    var y = 0;
                    while(y<9) {
                        if(this.dataL[x][y]===undefined) {
                            var newdata = this.data.slice();
                            newdata.splice(newdata.length, 0, [(last_play==='x'?'y':'x'),[x,y]]);
                            returner.push(state_factory(newdata, this.wins.slice()));

                        };
                        y++;
                    };
                    x++;
                };
            };
            return returner;
        };
    },

    fix() {
        this.dataL = [[],[],[],[],[],[],[],[],[],];
        for(i in this.data) {
            this.dataL[this.data[i][1][0]][this.data[i][1][1]] = this.data[i][0];
        };
        this.has_won = this.is_win();
        return this;
    },

    update_win() {
        var x = 0;
        var wins = [];
        while(x<9) {
            if(this.wins[x]===undefined) {
                wins[x] = this.is_local_win(x);
            } else {
                wins[x] = this.wins[x];
            };
            x++;
        };
        return wins;
    },

    score() {
        var last_play = this.data[this.data.length-1][0];
        if(this.has_won===undefined) {
            var sum = 0; 
            this.update_win().every(i=>{if(last_play===i){sum++}else if(i===undefined){}else{sum--}});
            var oldsum = 0;
            this.wins.every(i=>{if(last_play===i){oldsum++}else if(i===undefined){}else{oldsum--}});
            return sum - oldsum;
        } else {
            return (last_play===this.has_won)*4-2;
        };
    },

    is_win() {
        return this.is_local_win(this.update_win());
    },

    is_local_win(x) {
        var pwins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
        if(typeof(x)==='number') {
            x = this.dataL[x];
        };
        console.log(x);
        for(let i in pwins) {
            if(x[pwins[i][0]]===x[pwins[i][1]]&&x[pwins[i][1]]===x[pwins[i][2]]) {
                return x[pwins[i][0]];
            };
        };
        return undefined;
    },
};

function state_factory(data, win) {
    return Object.assign(Object.create(state), {data: data, wins:win}).fix();
};

module.exports = state_factory;
