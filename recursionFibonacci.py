def fib (position, x, y):
	if position == 1:
		return x
	if position == 2: #base case
		return y
	else: #recursive case
		temp = x + y
		x = y
		y = temp
		return fib(position - 1, x, y)

print (fib(10, 0, 1))  