def combine_sorted_lists(left, right):
    "combines the smaller sublists into larger sorted sublists"
    combined_list = []
    i = j = 0
    # adds the lower number from either left or right to combined_list until one list is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined_list.append(left[i])
            i += 1
        else:
            combined_list.append(right[j])
            j += 1
    # once a list is exhausted then append the numbers from the remaining list
    combined_list.extend(left[i:])
    combined_list.extend(right[j:])
    # return the larger sorted sublist
    return combined_list


def mergesort(mlist):
    "main function for breaking the original list into smaller sublists"
    if mlist is None:
        return None
    if len(mlist) == 0:
        return []
    if len(mlist) <= 1:
        return mlist
    # divide the list into two smaller lists
    middle = len(mlist) // 2
    left = mlist[:middle]
    right = mlist[middle:]
    # divide the smaller lists into even smaller lists recursively until
    # they are of length 1 or 0
    left = mergesort(left)
    right = mergesort(right)
    # return the combined sorted list of the current left/right sublists
    # building the final sorted list as the combined list grows
    return combine_sorted_lists(left, right)
