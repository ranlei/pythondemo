def binary_search(lists,n):
    """This algorithm is search n in list and we assume this list is sorted """
    low,high = 0,len(lists)-1
    while low<high:
        mid = (low+high)/2
        if lists[mid] > n:
            high = mid-1
        elif lists[mid] < n:
            low = mid+1
        else:
            return mid
        return -1

if __name__ == "__main__":
    a = [1,2,4,5,7,9]
    assert(binary_search(a,4) == 2)
    assert(binary_search(a,3) == -1)


