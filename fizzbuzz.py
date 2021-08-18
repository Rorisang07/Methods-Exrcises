def fizz_buzz(max):
    i = 0
    while i < max:
        i += 1

        if (i % 4 == 0 or i % 6 == 0) and not (i % 4 == 0 and i % 6 == 0):
            print(i)

fizz_buzz(15)