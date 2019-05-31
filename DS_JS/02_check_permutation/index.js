const checkPermutation = (str1, str2) => {
	str1 = str1.trim();
	str2 = str2.trim();

	if (str1.length !== str2.length)
		return false;

	if (str1 === str2)
		return true;

	const ascii = [];
	for (let i = 0; i < str1.length; i++) {
		if (typeof ascii[str1[i].charCodeAt()] === "undefined") {
			ascii[str1[i].charCodeAt()] = 1;
			continue;
		}
		ascii[str1[i].charCodeAt()] += 1;
	}

	for (let i = 0; i < str2.length; i++) {
		if (typeof ascii[str2[i].charCodeAt()] === "undefined") {
			return false;
		}
		ascii[str2[i].charCodeAt()]--;
	}

	return true;
};

console.log(checkPermutation("god","dog"));

module.exports = {
    checkPermutation,
}