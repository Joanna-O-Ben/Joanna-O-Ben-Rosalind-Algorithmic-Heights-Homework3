def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        k, m = file.readline().split()
        print(k, m)
        for n in range(int(k)):
            n = file.readline().split()
            lists = list(map(int, n))

            lst = []
            l = []
            p = 0
            flag = True
            while p < len(lists) and flag == True:
                if (lists[p]) * -1 in lists[p + 1:]:
                    l.append(p + 1)
                    l.append(lists[p + 1:].index(lists[p] * -1) + 1 + (p + 1))
                    lst.append(l)
                    flag = False
                p += 1

            if len(l) == 0:
                lst.append([-1])
            for i in lst:
                print(*i)


function("rosalind_2sum")