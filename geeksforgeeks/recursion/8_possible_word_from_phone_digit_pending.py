'''
Given a keypad as shown in diagram, and an N digit number. List all words which are possible by pressing these numbers.

Input Format:
The first line of input contains an integer T denoting the number of test cases. 
T testcases follow. Each testcase contains two lines of input. The first line of each test case is N, N is the number of digits. 
The second line of each test case contains D[i], N number of digits.

Output Format:
Print all possible words from phone digits with single space.

Your Task:
This is a function problem. You just need to complete the function possibleWords that takes an array as parameter 
and prints all the possible words. The newline is automatically added by the driver code.

Constraints:
1 <= T <= 10
1 <= N <= 10
2 <=  D[i] <= 9

Example:
Input:
2
3
2 3 4
3
3 4 5

Output:
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
dgj dgk dgl dhj dhk dhl dij dik dil egj egk egl ehj ehk ehl eij eik eil fgj fgk fgl fhj fhk fhl fij fik fil

Hints:

1) Try to use hash with recursion.
2) Let’s do some calculations first. How many words are possible with seven digits with each digit representing n letters? For first digit we have at most four choices, and for each choice for first letter, we have at most four choices for second digit and so on. So it’s simple maths it will be O(4n). Since keys 0 and 1 don’t have any corresponding alphabet and many characters have 3 characters, 4n would be the upper bound of number of words and not the minimum words.

Now let’s do some examples.
For number above 234. Do you see any pattern? Yes, we notice that the last character always either G,H or I 
and whenever it resets its value from I to G, the digit at the left of it gets changed.


Similarly whenever the second last alphabet resets its value, the third last alphabet gets changes and so on. 
First character resets only once when we have generated all words. This can be looked from other end also. 
That is to say whenever character at position i changes, character at position i+1 goes through all possible characters 
and it creates ripple effect till we reach at end.

Since 0 and 1 don’t have any characters associated with them. we should break as there will no iteration for these digits.

Let’s take the second approach as it will be easy to implement it using recursion. We go till the end and come back one by one. 
Perfect condition for recursion. let’s search for base case.
When we reach at the last character, we print the word with all possible characters for last digit and return. Simple base case.
When we reach at the last character, we print the word with all possible characters for last digit and return. Simple base case.

def possibleWords(a,N):

'''