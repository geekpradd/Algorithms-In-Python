from __future__ import division 

def sieve_of_eratosthenes(n):
	"""
	Sieve of Eratosthenes is used for finding prime number upto n.

	This function returns a list of prime numbers. And did I mention that it is bloody fast?
	Primes upto 13000 are calculated in 0.4 seconds in CPython. And don't even mention PyPy.

	"""
	from math import sqrt 
	factors = lambda a: [x for x in range(1,a+1) if not a%x]
	is_prime = lambda a: len(factors(a)) == 2

	def delete_multiples(array, element):
		for a,b in enumerate(array):
			if not b%element and b!=element:
				del array[a]
		return array 

	def primes_upto(n):
		"""
		Since using the sieve of erasthothenes, the square root is generally small use the iterative method
		"""
		return (x for x in range(1,n+1) if is_prime(x))

	limit = int(sqrt(n))
	numbers = list(range(2,n+1))
	for element in primes_upto(limit):
		numbers = delete_multiples(numbers,element)
	return numbers

def collatz_conjecture(n):
	"""
	Collatz Conjectures are a mathematical phenomenon where every number following a set of processes ends up becoming one.

	The processes are:
	 Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
	
	Returns a list containing the numbers (as per sequences)
	"""
	if n>1:
		seq = [n]
		while n!=1:
			if not n%2:
				n = n//2
			else:
				n = n*3+1
			seq.append(n)
		return seq 
	else:
		raise ValueError("N should be >1")


def merge_sort(array, log=False):
	"""
	Merge Sort is used for Sorting an iterable data structure which is a container and is mutable(set, list)
	
	Merge Sort is faster than Bubble Sort for larger data structures
	"""
	def merge(a,b):
		c = []
		while len(a) and len(b):
			if a[0]>b[0]:
				c.append(b[0])
				del b[0] 
			else:
				c.append(a[0])
				del a[0]
		while len(a):
			c.append(a[0])
			del a[0] 
		while len(b):
			c.append(b[0])
			del b[0]
		return c
	if len(array) == 1:
		return array 
	l1 = merge_sort(array[:len(array)//2:])
	l2 = merge_sort(array[len(array)//2::])
	if log:
		print (l1)
		print (l2)

	return merge(l1,l2)

def binary_search(element, array):
	"""
	Binary Search is used for retriving the index of an element in a data container 

	Returns -1 if not present
	"""
	if not element in array:
		return -1
	low, high = 0, len(array)-1
	mid =  low+high//2 
	array = bubble_sort(array)
	
	while array[mid] != element:
		if array[mid] > element:
			high = mid - 1 
			mid = low+high//2  
		else:
			low = mid + 1 
			mid = low+high//2  

	return mid

def bubble_sort(array):
	"""
	Bubble Sort is used for Sorting an iterable data structure which is a container and is mutable(set, list)
	
	Works very fast with small data containers
	"""
	passes = 0
	while True:
		swaps = 0 
		for index in range(len(array)-1):
			if array[index] > array[index+1]:
				array[index], array[index+1] =  array[index+1], array[index]
				swaps +=1 
		passes +=1
		if not swaps:
			break 
	return array

if __name__ == '__main__':

	print(sieve_of_eratosthenes(11330))