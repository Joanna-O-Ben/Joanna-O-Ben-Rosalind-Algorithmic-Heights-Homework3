def count_inv(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0

    for i in range(n):

        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = file.readline()
        lst = file.read().split(" ")
        lst = list(map(int, lst))

        return count_inv(lst)


print(function("rosalind_inv"))