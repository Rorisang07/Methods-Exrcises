def is_palindrome(word):
    if list(word) == list(reversed(word)):# list converts string itno a list so that i can be able to access each character
        print(True)
    else:
        print(False)
is_palindrome('level')




def average_of_three(num1, num2, num3):
    average = num1 + num2 + num3 // 3
    print(average)

average_of_three(7, 16 , 3)

def  goodbye(name):
    return  'It was nice meeting you ' + name + ', goodbye.'

print(goodbye('Rorisang'))