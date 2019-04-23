"""check prime number"""


def factorial(n):
	res = 1
	for i in range(1, n + 1):
		res *= i
	return res


def is_prime(n):
	# if (n - 1)! + 1 is divisible by n, then n is a prime number
	n_factorial = factorial(n - 1)
	n_factorial += 1
	res = False
	if n > 1 and n_factorial %n == 0:
		res = True
	return res

# Enter a number n, then show the n-first not prime numbers 
n = (int)(raw_input('Number: '))
iteration = 0
number = 1
res = []
prime_numbers_found = 0

while 1:
	if not is_prime(number):
		res.append(number)
		iteration += 1
	number += 1
	if iteration >= n:
		for i in res:
			print '{}'.format(i)
		break;	


