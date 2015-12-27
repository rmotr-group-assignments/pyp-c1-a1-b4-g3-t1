import sys

def recursive_fibonacci(n, fibvalues=(0, 1)):
    if n == 0:
        return fibvalues[0]
    return recursive_fibonacci(n - 1, (fibvalues[1], fibvalues[0] + fibvalues[1]))

def iterative_fibonnaci(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
        
    return a
    
def prompt_recursive():
    user_option = raw_input("Use recursive function? ").lower()
    if user_option == "y":
        return True
    elif user_option == "n":
        return False
    else:
        raise ValueError()
    
    
def get_n():
    user_n = int(raw_input("Nth fibonacci number? "))
    if user_n < 0:
        raise ValueError()
    return user_n
    
def main(init_recursive):
    try:
        user_n = get_n()
    except ValueError:
        print "Fibonnaci Number must be non-negative"
        return
    
    try:
        recursive = True if init_recursive else prompt_recursive()
    except ValueError:
        print "Must pass Y or N"
        return
        
    fib_num = recursive_fibonacci(user_n) if recursive else iterative_fibonnaci(user_n)
    print fib_num

if __name__ == '__main__':
    init_recursive = "--recursive" in sys.argv
    main(init_recursive)