'''
1. You are given a string, which represents an expression having only opening and closing parenthesis.
2. You have to remove minimum number of parenthesis to make the given expression valid.
3. If there are multiple answers, you have to print all of them.


Sample Input:

()())()

Sample Output:

(())()
()()()


https://www.youtube.com/watch?v=Cbbf5qe5stw&list=PL-Jc9J83PIiHO9SQ6lxGuDsZNt2mkHEn0&index=17

'''
from collections import deque

def getMin(str):
    
    st = deque()
    
    for i in range(len(str)):
        
        if(str[i] == '('):
            st.append(str[i])
            
        elif(str[i] == ')'):
            
            if(len(st) == 0):
                st.append(str[i])
                
            elif(st[-1] == ')'):
                st.append(str[i])
                
            elif(st[-1] == '('):
                st.pop()
                
    return len(st)

def solution(str, minRemoveAllowed, mySet):
    
    if(minRemoveAllowed == 0):
        minRemovedNow = getMin(str)
        if(minRemovedNow == 0):
            if(str not in mySet):
                print(str)
                mySet.add(str)
                
        return
    
    for i in range(len(str)):
        
        left = str[:i] # we have used i and not i+1 because we need to skip bracket
        right = str[i+1:]
        solution(left+right, minRemoveAllowed - 1, mySet)


if __name__ == "__main__":
    
    str = "()())()"
    ansSet = set()
    minRemoveAllowed = getMin(str)
    solution(str, minRemoveAllowed, ansSet)