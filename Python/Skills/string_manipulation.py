#Level 1: start now

#Do these one at a time in a Python file or the REPL, without looking anything up. If you have to look something up, mark that drill and redo it tomorrow.

#Print every character of "hello" on its own line.
for n in "hello":
    print(n)
    
#Given s = "Password123", print its length, its first character and its last character.
s = "Password123"
print(len(s))
print(s[0])
print(s[-1])

#Import string and print the lowercase letters and the digits joined into one string.
import string
print((string.ascii_lowercase) + string.digits)

#Use random.choice to print one random digit.
import random
test = [1,2,3,4,5]
print(random.choice(test))
#Build a list of 5 random lowercase letters, then turn it into a single string with join.
#Ask the user for a number with input. If what they typed isn’t a whole number, print “invalid”. Otherwise print the number times 2.
#Ask a yes/no question. Make " YES ", "y" and "Yes" all count as yes.
#Given pw = "abc123", print True if it contains at least one digit. Use any.
#Remove every vowel from "programming" using join and not in.
#Shuffle the list ["a", "b", "c", "d"] and print it as one string.