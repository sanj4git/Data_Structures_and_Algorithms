# HuffMann Encode string

import heapq
from collections import defaultdict


class HuffNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq
    
    def __gt__(self, other):
        return self.freq > other.freq
    
def get_codes(root, codes, code):
    if root.char:
        codes[root.char] = code
    else:
        get_codes(root.left, codes, code + '0')
        get_codes(root.right, codes, code + '1')
    

def huffmann_encode(string):
    freq = defaultdict(int)
    for char in string:
        freq[char] += 1
    
    heap = []
    for char, freq in freq.items():
        heapq.heappush(heap, HuffNode(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        node = HuffNode(None, left.freq + right.freq)
        node.left = left
        node.right = right
        heapq.heappush(heap, node)

    root = heapq.heappop(heap)
    codes = {}
    get_codes(root, codes, '')
    encoded_string = ''
    for char in string:
        encoded_string += codes[char]

    return encoded_string, root

def huffmann_decode(string, root):
    decoded_string = ''
    node = root
    for char in string:
        if char == '0':
            node = node.left
        else:
            node = node.right
        
        if node.char:
            decoded_string += node.char
            node = root
    
    return decoded_string

encoded_string, root = huffmann_encode('hello')
print(encoded_string)
print(huffmann_decode(encoded_string, root))
    
