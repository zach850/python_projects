#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def is_palindrome():
    user_string = input("Give me a word? " )
    if user_string == user_string[::-1]:
        print(f"{user_string} is a palindrome")
    else:
        print(f"{user_string} is not a palindrome")
        
is_palindrome()