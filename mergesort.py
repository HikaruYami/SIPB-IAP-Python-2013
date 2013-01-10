def mergesort_descending(some_list):
    if (len(some_list) < 2):
        return some_list
    top_half = mergesort_ascending(some_list[:len(some_list)/2])
    bottom_half = mergesort_ascending(some_list[len(some_list)/2:])
    sorted_list = []
    while len(top_half) > 0 and len(bottom_half) > 0:
        if top_half[0] > bottom_half[0]:
            sorted_list.append(top_half.pop(0))
        else:
            sorted_list.append(bottom_half.pop(0))
    sorted_list.extend(top_half)
    sorted_list.extend(bottom_half)
    return sorted_list

def mergesort_ascending(some_list):
    if (len(some_list) < 2):
        return some_list
    top_half = mergesort_ascending(some_list[:len(some_list)/2])
    bottom_half = mergesort_ascending(some_list[len(some_list)/2:])
    sorted_list = []
    while len(top_half) > 0 and len(bottom_half) > 0:
        if top_half[0] > bottom_half[0]:
            sorted_list.append(top_half.pop(0))
        else:
            sorted_list.append(bottom_half.pop(0))
    sorted_list.extend(top_half)
    sorted_list.extend(bottom_half)
    return sorted_list
