def binary_search2(lst1, lst2):
    results = []
    for n in lst2:
        n = int(n)
        mid = len(lst1) // 2
        start = 0
        end = len(lst1)
        found = False
        while start <= end and not found:
            if n > lst1[mid]:
                start = mid + 1
            elif n < lst1[mid]:
                end = mid - 1
            else:
                results.append(mid + 1)
                found = True
            mid = (start + end) // 2
        if not found:
            results.append(-1)
    return results


print(binary_search2(lst1, lst2))