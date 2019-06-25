def iterPower(base, exp):
    '''
	 base: int or float.
	 exp: int >= 0
				 
	 returns: int or float, base^exp
	 '''
	 # Your code here
	 if exp == 0:
	 	return 1.0
	 sum = base
	 remaining = exp - 1
	 while (remaining > 0):
	 	sum =  sum * base
		remaining -= 1
	 return sum
