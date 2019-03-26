# Incorporates tuples, lists and disctionaries - all in a single use case



"""
Create a program to analyse song lyrics with the followinng three features/functions:
    - a frequency dictionary that maps strings to integers; Return type is a dictionary, format {word;frequency}
    - word(s) that appears most often. Return type is a tuple,  format (list, int) for ([List of most freq. occoring word(s)],frequency)
    - words that appear at-least x number of times (x - user input); Return type is a list of tuples, each tuple has format (word,freq)
    
Comment: Not entirely straightforward, but will get the job done
"""

s = "one two three one one two three three three five six six six six six six"

def word_freq(s):
    s = s.lower()
    L = s.split(" ") 
    L.sort()
    
    song_dict = {}
    freq = 1
    
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            freq +=1
        else:
            song_dict[L[i]] = freq
            freq = 1
    return song_dict
            
        
#quick test
word_freq(s)    


def freq_word(s,func):
    song_dict = word_freq(s)
    max_list = []
    max1 = 0
    
    for i in song_dict.keys():
        if song_dict[i]> max1:
            max1 = song_dict[i]
            
    for i in song_dict.keys():
        if song_dict[i]== max1:
            max_list.append(i)
            
    return (max_list,max1)

#quick test
freq_word(s,word_freq)    
    

def atleast_x(s,func1,x): #badly named function that returns a list of tuples
    song_dict = word_freq(s)
    output_list = []
       
    for i in song_dict.keys():
        if song_dict[i]>= x:
            output_list.append((i,song_dict[i]))
    return output_list

#quick test
atleast_x(s,word_freq,4)


"""
Happy to have written efficient code
"""
