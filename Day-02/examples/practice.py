import sys 

def add(x, y):
    a = x + y
    return(a)

def sub(x, y): 
    s = x - y
    return(s)

def random(x,y):
    r = x * y
    return(r)

x = float(sys.argv[1])
y = float(sys.argv[3])
op = sys.argv[2]

if op == "add":
    result = add(x,y)
    print(result)