# fibonaci list is summation of last two digits

def add(a, b, fib_list):
    if len(fib_list) > 10:
        return fib_list
    
    c = a + b
    if a not in fib_list:
        fib_list.append(a)
    if b not in fib_list:
        fib_list.append(b)
        
    fib_list.append(c)

    return add(b, c, fib_list)

a = b = c = 0
fib_list = []
print(add(0,1,fib_list))