def gcdRecur(a, b):
	'''
	a, b: positive integers
		      
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	# Your code here
	if b == 0:
		return a
	else:
		return gcdRecur(b, a%b)

"""
Note:
Answer borrowed from group discussion.
Need to further understand when time allows.

Refer to: https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
"""
