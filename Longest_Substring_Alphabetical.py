# a simple program that prints out the longest substring in a given string thats aplhabetical

s = 'azcbobobegghakl'
l = len(s)
longTmp = ""
longMax = ""

for i in range(l):
    longTmp = s[i]
    for j in range(i,l-1):
        if s[j+1]>= s[j]:
            longTmp = longTmp + s[j+1]
        else:
            break
    if len(longTmp) > len(longMax):
        longMax = longTmp

print("Longest substring in alphabetical order is: ",longMax)
