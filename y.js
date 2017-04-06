(function (y) { // use y as you please
  return y(function (fib) {
    return function /* fib */ (n) {
      return n <= 2 ? 1 : fib(n - 1) + fib(n - 2)
    }
  })(7)
})(function /* y */ (le) {
  // I intentionally made these F’s uppercase,
  // so it's easier to differentiate them from the f’s few lines below
  return (function (F) {
    return F(F)
  })(function (f) {
    return le(function (x) {
      return f(f)(x)
    })
  })
}) // 13
