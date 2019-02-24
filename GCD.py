# a set of programs to calculate the GCD of 2 numbers. 
# Two alternate approches have been identitied: one is iterative and the other is recursive

def gcdIter(a,b):
    if a>=b:
        for i in range(b,0,-1):
            if(a%i==0 and b%i==0):
                return i
        return 1
    else:
        for i in range(a,0,-1):
            if(b%i==0 and a%i==0):
                return i
        return 1
            
            
gcdIter(323,306)  #well done, this wasn't a cakewalk


def gcdRecur(a,b):
    
    if b%a==0:
        return a
    if a>=b:
        return gcdRecur(b,a%b)
    if b>a:
        return gcdRecur(b,a)
    
   
gcdRecur(10,5)
