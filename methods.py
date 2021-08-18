def is_palindrome(word):
    if list(word) == list(reversed(word)):# list converts string itno a list so that i can be able to access each character
        print(True)
    else:
        print(False)
is_palindrome('level')






