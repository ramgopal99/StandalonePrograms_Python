#Implementing Selection Sort

#creating an unsorted list
import random as r

L1 = []
for i in range(1,20,2):
    L1.append(i)

r.shuffle(L1) #note that this MUTATES the list


#Implementing Selection Sort

def sort_selection(L):
    
    print(L)
    n = len(L)
    
    for i in range(n):
        small = L[i]
        print(small)
        temp =0
        s=0
        for j in range(i+1,n):
            #print("j ",j)
            if L[j] < small:
                
                temp = small #temp= 5
                small = L[j] # small = 1
                L[j] = temp 
                L[i] = small
                s+=1
                #print(small)
    print(L)
           
#testing
sort_selection(L1)
