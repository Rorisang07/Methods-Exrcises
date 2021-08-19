def fizz_buzz(max):
    nums = []
    i = 0
    while i < max:

        if (i % 4 == 0 or i % 6 == 0) and not (i % 4 == 0 and i % 6 == 0):
            nums.append(i)
        i += 1
    
    print(nums)

fizz_buzz(20)