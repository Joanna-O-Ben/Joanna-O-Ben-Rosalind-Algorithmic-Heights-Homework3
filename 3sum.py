def function(file_name):
    with open("C:\\Users\\Admin\\Downloads\\" + file_name + ".txt", "r") as file:
        k, m = file.readline().split()
        #         print(k, m)
        for lines in range(int(k)):
            lines = file.readline().split()
            nums = list(map(int, lines))

            res = []

            n = sorted(nums)
            length = int(m)
            f = False

            for i in range(0, length - 2):

                if i > 0 and n[i] == n[i - 1]:
                    continue

                l = i + 1
                r = length - 1

                while i < l < r and f == False:
                    total = n[i] + n[l] + n[r]

                    if total < 0:
                        l += 1

                    elif total > 0:
                        r -= 1

                    else:
                        res.append(sorted([nums.index(n[i]) + 1, nums.index(n[l]) + 1, nums.index(n[r]) + 1]))

                        while l < r and n[l] == n[l + 1]:
                            l += 1
                        while l < r and n[r] == n[r - 1]:
                            r -= 1

                        f = True

                        l += 1
                        r -= 1

                if len(res) == 0 or l > r:
                    res.append([-1])

            print(*res, sep="\n")


function("rosalind_3sum")