def three_way_partition(a):
    p = a[0]
    l = []
    c = []
    r = []
    for el in range(len(a)):
        if a[el] < p:
            l.append(a[el])
        elif a[el] == p:
            c.append(a[el])
        else:
            r.append(a[el])

    print(*l, *c, *r)

def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = file.readline()
        lst = file.read().split(" ")
        lst = list(map(int, lst))
        # lst = file.read().splitlines()
        # arr = list(map(int, lst[1:]))
        #         print(lst)
        return three_way_partition(lst)


print(function("rosalind_par3"))