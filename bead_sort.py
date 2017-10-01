import itertools

def neg_list(l):
    return map(lambda x: -x, l)

def filter_neg(l):
    return itertools.ifilter(lambda x: x<0, l)

def filter_pos(l):
    return itertools.ifilter(lambda x: x>0, l)

def zeros(l):
    return list(itertools.ifilter(lambda x: x==0, l))

def columns(l):
    return [filter(None, x) for x in itertools.izip_longest(*l)]

def bead_sort_base(l):
    return map(len, columns(columns([[1] * e for e in l])))

def bead_sort(list):
    return neg_list(bead_sort_base(neg_list(filter_neg(list)))) + zeros(list) + bead_sort_base(filter_pos(list))

if __name__ == '__main__':
    input_str = input('Enter the list of numbers to be sorted')
    arr = [int(i) for i in input_str.split()]
    print('The list of numbers before sorting : {}'.format(arr))
    bead_sort(arr)
    print('The list of numbers after sorting : {}'.format(arr))
