#Add implementation
def add(x,y):
	return x+y

#Subtract implementation
def subtract(x,y):
	return x-y

#Multiply Implementation
def multiply(x,y):
	return x*y

#Divide Implementation
def divide(x,y):
	if y == 0:
		return DIVIDE_BY_0_ERROR
	else:
		return x/y
# Square implementation
def square(x):
	return x*x