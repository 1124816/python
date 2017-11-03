process.stdin.resume();
process.stdin.setEncoding('utf8');

console.log("hello");
move();
function move() {
    process.stdin.on('data', function (chunk) {
        console.log("move");
    });
};
