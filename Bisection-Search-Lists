#Implement bi-section search on a list
# use a list of first 100 odd numbers
L = []
for i in range(1,200,2):
    L.append(i)

def bisectionSearch(L,n):
    i = 0
    low = 0
    high = len(L)-1
    mid = int((low+high)*0.5)
    
    while True:
        if n > L[high] or n < L[low]:
            i+=1
            return False
        elif  n == L[high]:
            i+=1
            print("Iterations ",i)
            return i
        elif n  > L[mid]:
            low = mid
            mid = int((low+high)*0.5)
            i+=1
        elif n < L[mid]:
            high = mid
            mid = int((low+high)*0.5)
            i+=1
        elif n == L[mid]:
            i+=1
            print ("iterations ",i)
            return mid
        elif i > 1000:
            return -99
        
bisectionSearch(L,19)
