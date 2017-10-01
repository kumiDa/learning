def cocktail_sort(arr):
    for k in range(len(arr)-1, 0, -1):
        swap_flag = False
        for i in range(k, 0, -1):
            if arr[i]<arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swap_flag = True

        for i in range(k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_flag = True

        if not swap_flag:
            return arr

if __name__ == '__main__':
    input_str = input('Enter the list of numbers to be sorted')
    arr = [int(i) for i in input_str.split()]
    print('The list of numbers before sorting : {}'.format(arr))
    cocktail_sort(arr)
    print('The list of numbers after sorting : {}'.format(arr))
