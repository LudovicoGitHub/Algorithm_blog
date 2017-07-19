def my_function(number):
    my_number = int(number)
    if my_number > 0:
        if number == number[::-1]:
            return True
        else:
            return False
    else:
        if number[1::] == number[:0:-1]:
            return True
        else:
            return False
mine = input()
print(my_function(mine))
