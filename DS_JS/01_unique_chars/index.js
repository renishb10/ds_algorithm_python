// Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
// cannot use additional data structures?

const isUnique = (str) => {
	if (str.length > 256)
		return false;

	const asciiKeys = [];
	for (let i = 0; i < str.length; i++) {
		if (typeof asciiKeys[str[i].charCodeAt()] !== "undefined")
			return true;

		asciiKeys[str[i].charCodeAt()] = 1;
	}
	//console.log(asciiKeys);
	return false;
};

console.log(isUnique("Rahul"));

module.exports = {
    isUnique,
};