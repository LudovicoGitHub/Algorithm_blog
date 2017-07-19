def my_function(my_string):
    length = len(my_string) - 1
    for i in range(0,length):
        if my_string[i] == "(":
            if my_string[i+1] != ")":
                print("Problem")
                exit(1)
        if my_string[i] == "[":
            if my_string[i+1] != "]":
                print("Problem")
                exit(1)
        if my_string[i] == "{":
            if my_string[i+1] != "}":
                print("Problem")
                exit(1)
    print("Every bracket closes in the right order")
