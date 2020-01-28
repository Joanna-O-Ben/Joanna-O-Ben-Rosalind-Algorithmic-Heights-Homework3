def twoWP(A):
    p = A[0]
    i = -1
    l = []
    r = []

    for j in range(1, len(A)):
        if A[j] < p:
            l.append(A[j])
        elif A[j] > p:
            r.append(A[j])
            i += 1
            A[i], A[j] = A[j], A[i]

    print(*l, p, *r)


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = file.readline()
        lst = file.read().split(" ")
        lst = list(map(int, lst))
        # lst = file.read().splitlines()
        # arr = list(map(int, lst[1:]))
        #         print(lst)
        return twoWP(lst)


print(function("rosalind_par"))