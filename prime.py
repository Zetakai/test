import random

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
    print(f"Penjumlahan {x}+{y}=",x+y)

def ai(x):
    talk=""
    if (x.find("hi")>=0 or x.find("hello")>=0):
        talk+="hello sweety"
    if (x.find("add")>=0):
        y=[int(s) for s in x.split() if s.isdigit()]
        a=0
        for i in y:
         a+=i
        talk+=f" it's {a}"
    print(talk)
        
