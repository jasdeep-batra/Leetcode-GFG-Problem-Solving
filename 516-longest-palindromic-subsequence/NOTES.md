LPS is nothing but a variation of LCS. And it's a very amazing problem.
So the idea is:
LCS is DP.
How to recognise DP problems?
1 1/0 kanpsack
2. unbounded knapsack
3. 3. LCS
what was common among all types?
we are using matrix
​
what do you mean by a palindrome : abcba ==abcba
​
bbbab === babbb
reverse the string and find LCS of reversed and original string.
​
​
​
Q.) How to find LCS of two strings?
Ans.) To find LCS of two string we must compare each character of both the string.
On comparision there are 2 possiblities.
1 both the characters are matching
2 both the characters are different. If both the characters are different then again their are two possibilities.
1. we can include the character from first string and exclude from second string.
2. we can include the character from second string and exclude from first string.
​