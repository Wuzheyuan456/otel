def bubble_sort(arr, reverse=False):
    result = arr[:]
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if (result[j] > result[j + 1]) != reverse:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == '__main__':
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6], reverse=True))
    print(bubble_sort([]))
    print(bubble_sort([1]))
