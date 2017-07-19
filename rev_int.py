def my_function(number):
    length = len(number) - 1
    if number[length] == "0":
        print("Error, the reverse is overflow")
        exit()
    else:
        return number[::-1]
