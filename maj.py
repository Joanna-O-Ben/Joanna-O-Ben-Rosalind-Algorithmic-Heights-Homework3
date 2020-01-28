from collections import Counter


def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        lst = file.readlines()

        for lines in lst:
            lines = lines.split()

            m = dict(Counter(lines).most_common(1))
            for key in m:
                m[key] = int(m[key])
                if m[key] > len(lines) // 2:
                    print (key, end = " ")
                else:
                    print (-1, end = " ")


print (function("rosalind_maj"))