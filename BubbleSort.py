#implementing bubble sort on a list

#create a randomly sorted list
import random as r

L1 = []
for i in range(1,200,2):
    L1.append(i)

r.shuffle(L1) #note that this MUTATES the list


#sorting the list in ascending order

def sort_function(L):
    
    print(L)
    n = len(L)
    
    while True:
        s= 0 #counter for recording the number of swaps in the current pass
        for i in range(n-1):
            temp = 0
            if L[i+1] < L[i]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                s+=1
        if s == 0:
            print (L)
            return L
                
                
#testing
sort_function(L1)              
                
