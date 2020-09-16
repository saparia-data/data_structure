'''
Given a string S with repeated characters (only lowercase). 
The task is to rearrange characters in a string such that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.

Example 1:
Input:
S = geeksforgeeks
Output: 1
Explanation: All the repeated characters
of the given string can be rearranged so
that no adjacent characters in the
string is equal.

Example 2:
Input:
S = bbbabaaacd
Output: 1
Explanation: Repeated characters in the
string cannot be rearranged such that
there should not be any adjacent repeated
character.

https://iq.opengenus.org/rearrange-string-no-same-adjacent-characters/
https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/

'''
import heapq

def rearrangeString(s):
    
    res = ""
    
    freq_dis = [0 for i in range(26)]

    for char in s:
        freq_dis[ord(char) - ord('a')] += 1
        
    #print(freq_dis)
        
    # make list of pair of frequency and character, this will be use as our max heap
    # so freq is stored in negative of original and min heap is used
    # resulting in a max heap
    freq_pair = []
    for i in range(26):
        if freq_dis[i]: # IF char is in string
            freq_pair.append([-1*freq_dis[i],chr(ord('a')+i)]) # multiplying by -1 to have a max heap property in min heap
            
    #print(freq_pair)
    
    heapq.heapify(freq_pair) # heapify this list
    
    #print(freq_pair)
    
    prev_pair = [0,'$'] # temp variable to store previous pair in value
    
    while(len(freq_pair)):
        curr_pair = heapq.heappop(freq_pair)
        
        # push prev pair , if it is valid
        if prev_pair[1] !='$':
            heapq.heappush(freq_pair,prev_pair)

        # add char in resultant string
        res+=curr_pair[1]
        
        # decrease frequency and discard if it reaches 0
        # here as freq stored is negative, adding 1 to decrease its absolute
        curr_pair[0] += 1
        
        if curr_pair[0] == 0:
            prev_pair = [0,'$'] # no prev taken for this
            
        else:
            prev_pair = curr_pair # assign prev pair to this
            
    if len(res)==len(s):
        # we obtain a valid string
        return res
    else:
        return -1
    
    
s = "bbbaa"
print(rearrangeString(s))
