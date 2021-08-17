
def is_palindrome(word):
    if word[:2] == word[:-1]:
        return True
    else:
        return False
print(is_palindrome('level'))




def average_of_three(num1, num2, num3):
    average = num1 + num2 + num3 // 3
    return average

print(average_of_three(7, 16 , 3))

def  goodbye(name):
    return  'It was nice meeting you ' + name + ', goodbye'

print(goodbye('Rorisang'))