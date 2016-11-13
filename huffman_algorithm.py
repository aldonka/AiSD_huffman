codes = {}

def frequency(str):
    freqs = {}
    for ch in str:
        freqs[ch] = freqs.get(ch, 0) + 1
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
        # sum of frequency of min_two
        sum_min_last_2 = min_two[0][0] + min_two[1][0]
        # build tree
        tuple_list = new_truple_list + [(sum_min_last_2, min_two)]
    return tuple_list[0]


def tree_of_letters(tuple_tree):
    heap = tuple_tree[1]
    if type(heap) == type(''):
        return heap
    else:
        return (tree_of_letters(heap[0]), tree_of_letters(heap[1]))


def assign(list_tree):
    return assign_codes(list_tree, '')


def assign_codes(list_tree, start_val):
    heap = list_tree[1]
    if type(heap) == type(''):
        return (heap, start_val)
    else:
        return (assign_codes(heap[0], start_val + str(1)), assign_codes(heap[1], start_val + str(0)))


def codes_tuple(list_with_codes):
    global codes
    if type(list_with_codes[1]) == type(''):
        codes[list_with_codes[0]] = list_with_codes[1]
    else:
        codes_tuple(list_with_codes[0])
        codes_tuple(list_with_codes[1])



def count_t(freq_tuple, codes_tuple):
    t = 0
    for k,v in freq_tuple.iteritems():
        t += v + len(codes_tuple[k])
    return t


def huffman(l):
    freq = sort_freq(frequency(l))
    tree = build_tree(freq)
    tree_with_codes = assign(tree)
    # t = count_t(freq, tree_with_codes)
    codes_tuple(tree_with_codes)
    print codes
    print "T: %d" %count_t(frequency(l), codes)
    return tree_with_codes


def encode(filename):
    big_string = read_file(filename)
    tree_with_codes =  huffman(big_string)
    for k,v in codes.iteritems():
        big_string = big_string.replace(k, v)
    new_file = open(filename.replace(".txt.", '') + '_encoded.txt', "wb")
    new_file.write(big_string)
    new_file.close()
    return tree_with_codes


def read_file(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    return data

def decode(filename, tree_with_codes):
    return ''


n = 'ddomiiin'
# n = 'akkkkkaaaklkhjkhkhjkhkjkhkl$  $z#'
# freq = frequency(n)
# print freq
# print sort_freq(freq)
# print build_tree(sort_freq(freq))
# g = tree_of_letters(build_tree(sort_freq(freq)))
# print g
# print assign(build_tree(sort_freq(freq)))
# sum = sum_dic(freq)
# min = min_dic(freq)
# print freq
# print freq.__len__()
# print 'Rozmiar %d' % sum
# print ('Minium ', min)
print huffman(n)
encode('seneca.txt')
