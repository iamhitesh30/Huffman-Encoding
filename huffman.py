import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(data):
    return Counter(data)

def build_priority_queue(frequency):
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    return priority_queue

def build_huffman_tree(priority_queue):
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]

def generate_codes(node, prefix="", code={}):
    if node:
        if node.char is not None:
            code[node.char] = prefix
        generate_codes(node.left, prefix + "0", code)
        generate_codes(node.right, prefix + "1", code)
    return code

def encode_data(data, huffman_codes):
    return ''.join(huffman_codes[char] for char in data)

def decode_data(encoded_data, tree):
    decoded_str = ""
    current_node = tree
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_str += current_node.char
            current_node = tree
    return decoded_str

# Main execution
data = "hitesh"

# Step 1: Calculate frequency
frequency = calculate_frequency(data)
print("Frequency of characters:", frequency)

# Step 2: Build priority queue
priority_queue = build_priority_queue(frequency)

# Step 3: Build Huffman tree
huffman_tree = build_huffman_tree(priority_queue)

# Step 4: Generate Huffman codes
huffman_codes = generate_codes(huffman_tree)
print("Huffman Codes:", huffman_codes)

# Step 5: Encode data
encoded_data = encode_data(data, huffman_codes)
print("Encoded Data:", encoded_data)

# Step 6: Decode data
decoded_data = decode_data(encoded_data, huffman_tree)
print("Decoded Data:", decoded_data)
