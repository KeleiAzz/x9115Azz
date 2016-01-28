def do_twice(f, v):
    f(v)
    f(v)

def print_spam():
    print 'spam'

def print_twice(s):
	print s
	print s

def do_four(f, v):
	do_twice(f, v)
	do_twice(f, v)

do_four(print_twice, "spam")
