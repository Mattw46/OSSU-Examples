/*
	Problem 2
	1 point possible (ungraded)
	Assume s is a string of lower case characters.

	Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
*/

var count = 0;
s = "azcbobobegghakl";

for (var i = 0; i < s.length; i++) {
	if (s.charAt(i) == 'b' && s.length - i > 2) {
		if (s.charAt(i+1) == 'o' && s.charAt(i + 2) == 'b') {
			count++;
		}
	}
}

console.log("Number of times bob occurs is: " + count);
