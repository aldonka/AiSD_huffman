import os

codes = {}
encoded_size = 0
file_size = 0

def slicen(s, n, truncate=False):
    assert n > 0
    while len(s) >= n:
        yield s[:n]
        s = s[n:]
    if len(s) and not truncate:
        yield s


def frequency(str):
    freqs = {}
    for ch in str:
        freqs[ch] = freqs.get(ch, 0) + 1
    return freqs


def frequency2(str, group_len):
    freqs = {}
    while len(str) > 0:
        group = str[0:group_len]
        str = str[group_len:]
        freqs[group] = freqs.get(group, 0) + 1
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


def huffman(l, group_len=1):
    freq = sort_freq(frequency2(l,group_len))
    tree = build_tree(freq)
    tree_with_codes = assign(tree)
    codes_tuple(tree_with_codes)
    print codes
    print "T: %d" %count_t(frequency2(l,group_len), codes)
    return tree_with_codes


def encode(filename,encoded_filename, group_len=1):
    big_string = read_file(filename)
    global file_size, encoded_size
    file_size = os.path.getsize(filename)
    tree_with_codes = huffman(big_string, group_len)
    encoded_string = ""

    while len(big_string) > 0:
        group = big_string[0:group_len]
        big_string = big_string[group_len:]
        encoded_string += codes[group]

    new_file = open(encoded_filename, "wb")
    new_file.write(encoded_string)
    new_file.close()
    encoded_size = os.path.getsize(new_file)
    return tree_with_codes


def read_file(filename):
    with open(filename, 'r') as myfile:
        data = ""
        for line in myfile.readlines():
            data += line
    myfile.close()
    return data


def decode(filename, decoded_filename, tree_with_codes):
    encoded_string = read_file(filename)
    decoded_string = ""
    t = tree_with_codes
    print tree_with_codes
    for bit in encoded_string:
        if bit == '0' : t = t[1]
        else: t = t[0]
        if type(t[1]) == type(''):
            decoded_string += t[0]
            t = tree_with_codes
    new_file = open(decoded_filename, "wb")
    new_file.write(decoded_string)
    new_file.close()

n = 'ddomiiiin'
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
# print huffman(n)
# print huffman(n,2)
# print huffman(n,3)
# print huffman(n,4)
decode('seneca_encode.txt','seneca_dec.txt', encode('seneca.txt','seneca_encode.txt',4))
# decode('seneca_encoded.txt', encode('seneca.txt', 2))
print 'Size file: %d, size encoded: %d, K = %f' %(file_size, encoded_size,((file_size-encoded_size)/float(file_size)))
