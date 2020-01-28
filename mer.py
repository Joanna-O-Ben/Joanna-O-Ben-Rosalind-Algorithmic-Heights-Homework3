def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        n1 = file.readline().split()
        n2 = file.readline().split()

        n1 = list(map(int, n1))
        n2 = list(map(int, n2))

        for i in n2:
            n1.append(i)

        print(sorted(n1))


print (function("rosalind_mer"))