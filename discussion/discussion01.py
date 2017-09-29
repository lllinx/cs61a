def wears_jacket(temp, raining):
	"""
	>>> rain = False 
	>>> wears_jacket(90, rain)
	False
	>>> wears_jacket(40, rain)
	True
	>>> wears_jacket(100, True)
	True
	"""
	return raining or temp<60

def handle_overflow(s1, s2):
	"""
	>>> handle_overflow(27, 15)
	No overflow.
	>>> handle_overflow(35, 29)
	1 spot left in Section 2.
	>>> handle_overflow(20, 32)
	10 spots left in Section 1.
	>>> handle_overflow(35, 30)
	No space left in either section.
	"""
	if s1<30 and s2<30:
		return 'No overflow.'
	elif s1<30 and s2>=30:
		return '{} spot left in section 1.'.format(30-s1)
	elif s1>=30 and s2<30:
		return '{} spot left in section 2.'.format(30-s2)
	else:
		return 'No space left in either section.'

def is_prime(n):
	x=n-1
	while x>1:
		if n%x == 0:
			return False
		x=x-1
	return True

from operator import add
def sub(a, b):
	sub = add
	return a - b
add = sub
sub = min
print(add(2, sub(2, 3)))

def keep_ints(cond, n):
	"""Print out all integers 1..i..n where cond(i) is true
	>>> def is_even(x):
	... # Even numbers have remainder 0 when divided by 2.
	... return x % 2 == 0
	>>> keep_ints(is_even, 5)
	2
	4
	"""
	i=1
	while i <= n:
		if cond(i) == True:
			print(i)
		i += 1

def keep_ints(n):
	"""Returns a function which takes one parameter cond and
	prints out all integers 1..i..n where calling cond(i)
	returns True.
	>>> def is_even(x):
		# Even numbers have remainder 0 when divided by 2.
		return x % 2 == 0
	>>> keep_ints(5)(is_even)
	2
	4
	"""
	def f(cond):
		i=1
		while i<=n:
			if cond(i)==True:
				print(i)
			i += 1
	return f



