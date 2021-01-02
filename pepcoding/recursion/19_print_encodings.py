'''
1. You are given a string str of digits. (will never start with a 0)
2. You are required to encode the str as per following rules
    1 -> a
    2 -> b
    3 -> c
    ..
    25 -> y
    26 -> z
3. Complete the body of printEncodings function - without changing signature - to calculate and print all encodings of str.

Use the input-output below to get more understanding on what is required

123 -> abc, aw, lc
993 -> iic
013 -> Invalid input. A string starting with 0 will not be passed.
103 -> jc
303 -> No output possible. But such a string maybe passed. In this case print nothing.

Sample Input:

655196

Sample Output:

feeaif
feesf


https://www.youtube.com/watch?v=2ClSccwnq1Y&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=45

'''

def printEncodings(ques, asf):
    
    if(len(ques) == 0):
        print(asf)
        return
    
    elif(len(ques) == 1):
        
        if(ques[0] == '0'):
            return
        else:
            ch0 = ques[:1]
            roq0 = ques[1:]
            code0 = ord('a') + int(ch0) - 1
            printEncodings(roq0, asf + chr(code0))
    
    # if length of ques is 2 or greater than 2        
    else:
        
        if(ques[0] == '0'):
            return
        else:
            # taking only first int. i.e. out of 123, take ch0 = 1 and roq0 = 23
            ch0 = ques[:1]
            roq0 = ques[1:]
            code0 = ord('a') + int(ch0) - 1
            printEncodings(roq0, asf + chr(code0))
            
            # taking two ints. i.e. out of 123, take ch0 = 12 and roq0 = 3
            ch1 = ques[:2]
            roq1 = ques[2:]
            code1 = ord('a') + int(ch1) - 1
            if(int(ch1) <= 26):
                printEncodings(roq1, asf + chr(code1))
                
printEncodings("655196", "")
            
            
            
    
    
    
    
    
    