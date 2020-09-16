'''
Given two strings. Find the smallest window in the first string consisting of all the characters of the second string.

Input:
First line of the input contains an integer T, denoting the number of test cases. 
Then T test case follows. Each test contains 2 lines having a string S (the first string) and next line contains a string P (the second string).

Output:
Output the smallest window of the string containing all the characters of the text. 
If such window doesn`t exist or this task can not be done then print -1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestWindow() 
which takes two string S and P as inputs and returns the smallest window in string S having all the characters of the string P. 
In case there are multiple such windows of same length, return the one with the least starting index. Return "-1" in case there's no such window present. 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= |S|, |P| <= 1000

Example:
Input:
2
timetopractice
toc
zoomlazapzo
oza
Output:
toprac
apzo

Explanation:
Testcase 1: toprac is the smallest subset in which toc can be found.
Testcase 2: To find oza in the zoomlazapzo the smallest subset is apzo.

hints:

1)
First check if the length of string is less than the length of the given text, if yes then no such window can exist .
Try to use the concept of hashing to solve further cases.

2)
-Store the occurrence of characters of the given pattern in a hash table.
-Start matching the characters of pattern with the characters of string i.e. increment count if a character matches.
-Check if (count == length of text) this means a window is found.

3)
-If such window found, try to minimize it by removing extra characters from the beginning of the current window.
-Update min_length. Print the minimum length of window.

'''
def smallestWindow(s,p):
    if(len(p)>len(s)):
        return -1
    shash=[0 for i in range(26)]
    phash=[0 for i in range(26)]

    for char in p:
        phash[ord(char)-ord('a')]+=1
        
    print(phash)
    
    counter=0
    begin=0
    startindex=-1
    length=0
    minlength=1e10
    
    for i in range(len(s)):
        shash[ord(s[i])-ord('a')]+=1
        
        # If string's char matches with  
        # pattern's char then increment count  
        if(phash[ord(s[i])-ord('a')] != 0 and shash[ord(s[i])-ord('a')] <= phash[ord(s[i])-ord('a')]):
            counter+=1
        
        # if all the characters are matched 
        if(counter==len(p)):
            # Try to minimize the window i.e., check if  
            # any character is occurring more no. of times  
            # than its occurrence in pattern, if yes  
            # then remove it from starting and also remove  
            # the useless characters.
            while(shash[ord(s[begin])-ord('a')] > phash[ord(s[begin])-ord('a')] or phash[ord(s[begin])-ord('a')] == 0):
                if(shash[ord(s[begin])-ord('a')] > phash[ord(s[begin])-ord('a')]):
                    shash[ord(s[begin])-ord('a')] -= 1
                    begin += 1
                    
            # update window size 
            length = i- begin + 1

            if(length < minlength):
                startindex = begin
                minlength = length
    
    # If no window found
    if(startindex == -1):
        return "-1"
    else:
        # Return substring starting from  
        # start_index and length min_len
        return s[startindex:startindex+minlength]
    
s = "timetopractice"
p = "toc"
print(smallestWindow(s, p))