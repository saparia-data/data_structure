'''
1. You are given n space separated strings, which represents a dictionary of words.
2. You are given another string which represents a sentence.
3. You have to print all possible sentences from the string, such that words of the sentence are 
   present in dictionary.
   
   
Sample Input:

11
i like pep coding pepper eating mango man go in pepcoding
ilikepeppereatingmangoinpepcoding

Sample Output:

i like pepper eating man go in pep coding 
i like pepper eating man go in pepcoding 
i like pepper eating mango in pep coding 
i like pepper eating mango in pepcoding 


https://www.youtube.com/watch?v=LmHWIsBQBU4&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=16

'''
def wordBreak(str, asf, wordSet):
    
    if(len(str) == 0):
        print(asf)
        return
    
    for i in range(len(str)):
        
        left = str[:i+1]
        if(left in wordSet):
            right = str[i+1:]
            wordBreak(right, asf + left + " ", wordSet)


if __name__ == "__main__":
    
    str = "ilikepeppereatingmangoinpepcoding" 
    sentence = "i like pep coding pepper eating mango man go in pepcoding"
    
    wordSet = set(sentence.split(" "))
    #print(wordSet)
    
    wordBreak(str, "", wordSet)
    
    