function foo() {
    console.log(this.a);
};
var a = 4;
console.log(foo());
