# для данного случая можно рассмотреть несколько сортировок: quicksort, mergeSort

# quicksort в среднем работает за О(Nlog(n)) и имеет низкую константу,
# однако в худшем случае его время поднимается до O(N^2) что очень медленно
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# mergesort всегда работает за О(Nlog(n)) но имеет большую константу,
# поэтому на практике работает медленнее, чем quicksort
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    leftid, rightid = 0, 0

    while leftid < len(left) and rightid < len(right):
        if left[leftid] <= right[rightid]:
            sorted_arr.append(left[leftid])
            leftid += 1
        else:
            sorted_arr.append(right[rightid])
            rightid += 1

    sorted_arr.extend(left[leftid:])
    sorted_arr.extend(right[rightid:])

    return sorted_arr

# В итоге тк мы рассматриваем случай, в котором сортировки, работающие быстрее, чем за NlogN невозможно использовать,
# в большинстве случаев лучшим выбором будет quicksort,
# однако если набор данных для сортировки имеет тенденцию к худшим случаям, то стоит выбрать mergesort
