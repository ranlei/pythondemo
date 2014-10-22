def quicksort(lists,left,right):
    """Pivot point to start here"""
    if left < right:
        i = left
        j = right
        key = lists[i]
        while i<j:
            while i<j and lists[j]>=key:
                j -=1
            if i<j:
                lists[i] = lists[j]
                i -= 1
            while i<j and lists[i]<key:
                i += 1
            if i<j:
                lists[j] = lists[i]
                j -= 1
        lists[i] = key
        quicksort(lists,left,i-1)
        quicksort(lists,i+1,right)
        
if __name__ == "__main__":
    lists = [5,4,3,2,1,0]
    print (lists)
    quicksort(lists,0,len(lists)-1)
    print (lists)










