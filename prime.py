
def getprime(x,y):
    a = range(x,y)
    z = []
    prime = True
    for i in a:
        prime = True
        for j in range(2, i):
            if (i % j == 0):
                prime = False
                break
        if (prime == True):
            if (i > 1):
                z.append(i)
    print(z)

def addition(x,y):
    print(x+y)
