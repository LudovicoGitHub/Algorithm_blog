
def my_function(array,target):
    length = len(array) - 1
    flag = 0
    i = 0
    j = length
    while flag == 0 and i < length and j >= 0:
        if array[i] + array[j - i] == target:
            flag = 1
            index_1 = i
            index_2 = j - i
        elif array[i] + array[j - i] < target:
            i = i + 1
        else:
            j = j - 1


    if flag == 1:
        return index_1,index_2
    else:
        print("No matching found")
        exit()

print("Please insert target number: ")
choiche = input()
number = int(choiche)
my_arr = [1,3,6]
running = my_function(my_arr,number)
print(running)
