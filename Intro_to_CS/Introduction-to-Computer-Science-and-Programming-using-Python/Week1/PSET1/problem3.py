"""
Problem 3
15/15 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""


longest = ""
temp = ""

for i in range(len(s) - 1):
    
    
    if len(temp) > len(longest):
        longest = temp
        temp = ""
    
    if s[i] <= s[i + 1]:
        
        temp = s[i] + s[i + 1]
        
        """ look for next match """
        curr = i + 1
        nxt = curr + 1
        while (curr < len(s) - 1):
            
            if s[curr] <= s[nxt]:
                temp += s[nxt]
                
            else:
                break
            curr += 1
            nxt += 1

""" if longest not found (two chars) return the first element"""            
if len(longest) == 0:
    longest = s[0]  
          
print("Longest substring in alphabetical order is: " + longest)