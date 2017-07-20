def my_function(number):
    stringed = str(number)
    length = len(stringed) - 1

    if stringed[length] == "0":
        print("Error, the reverse is overflow")
        exit()
    if number > 0:
        return stringed[::-1]
    else:
        return "-" + stringed[:0:-1]
