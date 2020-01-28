def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = int(file.readline())
        lst = file.readline().split(" ")
        lst = list(map(int, lst))
        k = int(file.readline())

        lst = sorted(lst)
        result = lst[k - 1]

        return result


#         print(type(n), n, type(lst), lst, type(k), k, sep = "\n")

print(function("rosalind_med"))