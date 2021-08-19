def fizz_buzz(max):
    number = []
    i = 0
    while i < max:

        if (i % 4 == 0 or i % 6 == 0) and not (i % 4 == 0 and i % 6 == 0):
            number.append(i)
        i += 1
    
    print(number)

fizz_buzz(30)

