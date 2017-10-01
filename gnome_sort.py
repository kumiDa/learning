def gnomeSort(arr):
    i = 0
    n = len(arr)
    while i < n:
        if i and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        else:
            i += 1
    return

def teleportingGnomeSort(arr):
    i = j = 0
    n = len(arr)
    while i < n:
        if i and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        else:
            if i < j: 
                i = j
            j = i = i+1
    return

if __name__ == '__main__':
    input_str = input('Enter the list of numbers to be sorted')
    arr = [int(i) for i in input_str.split()]
    print('The list of numbers before sorting : {}'.format(arr))
    gnomeSort(arr)
    print('The list of numbers after sorting : {}'.format(arr))
