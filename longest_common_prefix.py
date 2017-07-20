def my_function(a):
    n = len(a) - 1
    k = len(a[0]) - 1
    for i in range(k,0,-1):
        counter = 0
        for j in range(1,n):
            if a[0][:i:] == a[j][:i:]:
                counter = counter + 1
            if counter == n-1:
                print("The longest common prefix has length",i)
                exit()
    print("There is no longest common prefix")
