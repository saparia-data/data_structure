'''
1. You are given a string str of digits. (will never start with a 0)
2. You are required to encode the str as per following rules
    1 -> a
    2 -> b
    3 -> c
    ..
    25 -> y
    26 -> z
3. You are required to calculate and print the count of encodings for the string str.

     For 123 -> there are 3 encodings. abc, aw, lc
     For 993 -> there is 1 encoding. iic 
     For 013 -> This is an invalid input. A string starting with 0 will not be passed.
     For 103 -> there is 1 encoding. jc
     For 303 -> there are 0 encodings. But such a string maybe passed. In this case 
     print 0.
     

Sample Input:

123
21123

Sample Output:

3
8


https://www.youtube.com/watch?v=jFZmBQ569So&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=20


'''

def countEncodings(str):
    
    dp = [0] * len(str)
    dp[0] = 1
    
    for i in range(1, len(dp)):
        
        if(str[i - 1] == '0' and str[i] == '0'):
            dp[i] = 0
        elif(str[i - 1] == '0' and str[i] != '0'):
            dp[i] = dp[i - 1]
        elif(str[i - 1] != '0' and str[i] == '0'):
            if(str[i - 1] == '1' or str[i - 1] == '2'): # check if last two digit is less than 26
                dp[i] = (dp[i - 2] if i >=2 else 1)
            else:
                dp[i] = 0
        else:
            if(int(str[i-1: i+1]) <= 26): # check if last two digit is less than or equal to 26
                dp[i] = dp[i - 1] + (dp[i - 2] if i >=2 else 1)
            else:
                dp[i] = dp[i - 1]
                
                
    return dp[len(str) - 1]
                




if __name__ == "__main__":
    
    str = "21123"
    print(countEncodings(str))