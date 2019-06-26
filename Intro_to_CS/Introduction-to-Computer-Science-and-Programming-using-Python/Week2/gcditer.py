def gcdIter(a, b):
	'''
	a, b: positive integers
		      
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	# Your code here
	if a < b:
		divisor = a
	else:
		divisor = b
	    
	while divisor > 1:
		if (a % divisor == 0) and ( b % divisor == 0):
			return divisor
		divisor -= 1
	return 1


print(gcdIter(2,12))     
print(gcdIter(6,12))     
print(gcdIter(9,12))  
print(gcdIter(17,12))  
