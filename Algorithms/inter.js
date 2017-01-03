var arr = [1,2,3,1,3,3,1];
var loc = [];
var num = [];
var max = 0;

for (var i = 0; i < arr.length; i++) {
  if (arr[i]>num[num.length-1]||num.length==0) {
    num.push(arr[i]);
    loc.push(i)
  }else if(arr[i]<num[num.length-1]) {
    while (arr[i]<num[num.length-1]) {
      if ((i-loc[num.length-1])*num[num.length-1]>max) {
        max = (i-loc[num.length-1])*num[num.length-1];
      };
      temp = loc[num.length-1]
      num.pop();
      loc.pop();
    };
    num.push(arr[i]);
    loc.push(temp);
  };
};

for (var p = 0; p < num.length;p++) {
  if (((arr.length)-loc[p])*num[p]>max) {
    max = ((arr.length)-loc[p])*num[p];
  };
};
console.log(max);
