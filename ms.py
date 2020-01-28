def mergeSort(ar):
    return (sorted(ar))


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n = file.readline().split()
        n = list(map(int, n))

        return mergeSort(n)


print (function("rosalind_ms"))