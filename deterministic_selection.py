# deterministic_selection.py
def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select_median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    pivot = select_median_of_medians(medians, len(medians)//2)
    pivot_index = arr.index(pivot)
    pivot_index = partition(arr, 0, len(arr)-1, pivot_index)
    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return select_median_of_medians(arr[:pivot_index], k)
    else:
        return select_median_of_medians(arr[pivot_index+1:], k - pivot_index - 1)
