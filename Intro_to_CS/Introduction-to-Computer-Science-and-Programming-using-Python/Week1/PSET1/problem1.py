"""
Problem 1
0.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

"""

vowels = ["a", "e", "i", "o", "u"]
s = 'azcbobobegghakl'
count = 0

for i in range(len(s)):
	if s[i] in vowels:
		count += 1

print(count)
