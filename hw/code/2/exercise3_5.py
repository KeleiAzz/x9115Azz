def do_twice(f, v):
	f(v)
	f(v)

def do_four(f, v):
	do_twice(f, v)
	do_twice(f, v)

def print_grid():
	print_horizontal()
	print_vertical()
	print_horizontal()
	print_vertical()
	print_horizontal()

def print_horizontal():
	print "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+"

def print_vertical():
	print "/", " ", " ", " ", " ", "/", " ", " ", " ", " ", "/"
	print "/", " ", " ", " ", " ", "/", " ", " ", " ", " ", "/"
	print "/", " ", " ", " ", " ", "/", " ", " ", " ", " ", "/"
	print "/", " ", " ", " ", " ", "/", " ", " ", " ", " ", "/"

print_grid()