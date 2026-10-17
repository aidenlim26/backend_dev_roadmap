#Develop a password generator that creates random, secure passwords based on user-defined criteria (e.g., length, inclusion of special characters). 
#This project will help you understand random number generation and string handling.

import secrets
import string


def get_length():
    valid = False
    while valid == False:
        length = str(input("Enter a length: ")).strip()
        if length.isdigit() == False:
            print("Must be a whole number")
            continue

        length = int(length)

        if (length < 8) or (length > 64):
            print("Must be between 8-64")
            continue
        else:
            valid = True

    return length
    


def ask_yes_no(question):
    answer = input(question).strip().lower()

    return answer in ("y","yes")



def build_pool(use_upper, use_digits, use_symbols):
    # start: pool = lowercase letters, categories = [lowercase letters]
    pool = string.ascii_lowercase
    categories = ["lowercase letters"]

    if use_upper:
        categories.append(string.ascii_uppercase)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        categories.append(string.punctuation)

    pool = "".join(categories)
    return pool, categories


def generate(length, pool, categories):
    if length < len(categories):
         raise ValueError("Password length must be at least the number of categories")
    
    chars = []

    for category in categories:
         chars.append(secrets.choice(category))

    while len(chars) < length:
         chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(chars)

    return "".join(chars)



def main():
    question = str(input("Do you want to include special characters in your password?: ")).strip().lower() 
    length = get_length()
    
    use_upper = ask_yes_no("Do you want to use uppercase?: ")
    use_digits = ask_yes_no("Do you want to use digits?: ")
    use_symbols = ask_yes_no("Do you want to use symbols?: ")

    pool,categories = build_pool(use_upper,use_digits,use_symbols)

    password = generate(length,pool,categories)

    print("Your password:", password)

    

main()