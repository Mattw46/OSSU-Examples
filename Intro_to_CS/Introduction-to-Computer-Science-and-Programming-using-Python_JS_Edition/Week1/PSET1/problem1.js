/*
Problem 1
0.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

*/

var vowels = ['a','e','i','o','u'];
var s = 'azcbobobegghakl';
var count = 0;

for (var i = 0; i < s.length; i++) {
    for (var j = 0; j < vowels.length; j++) {
        if (s.charAt(i) == vowels[j]) {
			count++;
			break;
		  }
    }
}

console.log("Number of vowels: " + 5);
