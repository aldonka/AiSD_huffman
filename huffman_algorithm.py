def frequency(str):
    freqs = {}
    for ch in str:
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs


def sum_dic(dictionary):
    sum = 0
    for k, v in dictionary.iteritems():
        sum += dictionary[k]
    return sum


def min_dic(dictionary):
    minimal_element = sum_dic(dictionary)
    minimal_dic = {}
    for k, v in dictionary.iteritems():
        if dictionary[k] < minimal_element:
            minimal_element = dictionary[k]
            minimal_dic.clear()
            minimal_dic[k] = minimal_element
        elif dictionary[k] == minimal_element:
            minimal_dic[k] = minimal_element
    return minimal_dic


def sort_freq(freqs_dic):
    truples = []
    for k, v in freqs_dic.iteritems():
        truples.append((v, k))
    truples.sort()
    return truples


def build_tree(tuple_list):
    while len(tuple_list) > 1:
        min_two = tuple(tuple_list[0:2])
        new_truple_list = tuple_list[2:]
        #sum of frequency of min_two
        sum_min_last_2 = min_two[0][0] + min_two[1][0]
        # build tree
        tuple_list = new_truple_list + [(sum_min_last_2, min_two)]
    return tuple_list[0]


def tree_of_letters(tuple_tree):
    heap = tuple_tree[1]
    if type(heap) == type(''): return heap
    else: return (tree_of_letters(heap[0]), tree_of_letters(heap[1]))

def assign(list_tree):
    return assign_codes(list_tree, '')


def assign_codes(list_tree, start_val):
    heap = list_tree[1]
    if type(heap ) == type('') : return (heap, start_val)
    else:return (assign_codes(heap[0], start_val+str(1)),assign_codes(heap[1], start_val+str(0)))


def count_t(freq, tree_with_codes):
    return 0


def huffman(l):
    freq = sort_freq(frequency(l))
    tree = build_tree(freq)
    tree_with_codes = assign(tree)
    t = count_t(freq, tree_with_codes)
    return tree_with_codes


n = 'aaaellklklllkkklbbbg'
# n = 'akkkkkaaaklkhjkhkhjkhkjkhkl$  $z#'
freq = frequency(n)
print sort_freq(freq)
print build_tree(sort_freq(freq))
g = tree_of_letters(build_tree(sort_freq(freq)))
print g
print assign(build_tree(sort_freq(freq)))
sum = sum_dic(freq)
min = min_dic(freq)
print freq
print freq.__len__()
print 'Rozmiar %d' % sum
print ('Minium ', min)
print huffman(n)