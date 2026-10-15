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
random_lower = [0]*5
n = 0
while n < 5:
    random_lower[n] = random.choice(string.ascii_lowercase)
    n = n+1

print("".join(random_lower))

#Ask the user for a number with input. If what they typed isn’t a whole number, print “invalid”. Otherwise print the number times 2.
user_input = str(input("Enter a number: "))

try:
    new_user_input = int(user_input)
    print(new_user_input)
    print(new_user_input)
except TypeError:
    print("Input needs to be a whole number")
except ValueError:
    print("Input needs to be a whole number")
except Exception:
    print("Input needs to be a whole number")

#Ask a yes/no question. Make " YES ", "y" and "Yes" all count as yes.
ynquestion = str(input("Do you like bananas?: "))
answer = ynquestion.strip().lower()

if (answer == "yes") or (answer == "y"):
    print("Successful")
elif ynquestion == "YES":
    print("Successful")
else:
    print("Unsuccessful")

#Given pw = "abc123", print True if it contains at least one digit. Use any.
pw = "abc123"
found = False
j = 0
while j < len(pw):
    if pw[j].isdigit():
        found = True
        break
    else:
        j = j + 1
        continue
print(found)

#Remove every vowel from "programming" using join and not in.
#Shuffle the list ["a", "b", "c", "d"] and print it as one string.