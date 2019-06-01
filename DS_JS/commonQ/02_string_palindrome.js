const isPalindrome = function(str){
  // if want we can convert it to lowercase if case insensitive
  str = str.toLowerCase();
  const mid = Math.floor(str.length/2);
  for(let i=0; i<mid; i++) {
    if (str[i] !== str[str.length - 1 - i])
      return false;
  }
  return true;
};

console.log(isPalindrome("anna"));