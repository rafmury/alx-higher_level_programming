#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None

    lo, hi = 0, len(list_of_integers)

    while lo < hi:
        mid = (hi + lo) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid < len(list_of_integers) - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return None  # Should not reach here if the list is not empty

