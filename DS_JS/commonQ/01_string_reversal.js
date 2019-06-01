(function reverseString(str) {
  if (typeof str === "string" || str instanceof String) {
    let result = '';
    for(let i=str.length-1; i>=0; i--) {
      result = result + str[i];
    };
    console.log(result);
    return result;
  }
  return str;
})("Hello");