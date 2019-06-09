// Palindrome Permutation: Given a string, write a function to check if it is a permutation of
// a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
// permutation is a rearrangement of letters. The palindrome does not need to be limited to just
// dictionary words.
// EXAMPLE
// Input: Tact Coa
// Output: True (permutations: "taco cat'; "atc o eta·; etc.)

function palindromePerm(str) {
  if (str.length > 0) {
    let dict = {};
    str = str.toLowerCase().replace(/ /g, '');
    for (let i=0; i<str.length; i++) {
      if (dict[str[i]]) {
        dict[str[i]] += 1;
      }
      else {
        dict[str[i]] = 1;
      }
    }

    let count = 0;
    for (let key in dict) {
      if (dict[key] % 2 !== 0)
        count++;
    }

    return count > 1 ? false : true;
  }
};

console.log(palindromePerm("Tact Coa"));
console.log(palindromePerm("malayalam"));
console.log(palindromePerm("anna"));