import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # print(f)
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # print(p.qsize())
    # print(p.queue )
    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        x = p.get()
        y = p.get()
        # print(x.children())
        p.put(TreeNode(x,y,(x.data[0]+y.data[0],"")))

    # print(p.qsize())
    # print(p.get().children())
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # print(prefix)
    # try:
    #     print(f'{node.data}, {node.left.data}, {node.right.data}')
    # except:
        # pass
    if node.left is None and node.right is None:  # reached a leaf node
            code[node.data[1]] = prefix  # assign the binary encoding to the character
    else:
        if node.left:
            get_code(node.left, prefix + '1', code)
            # node.left.assign_codes(prefix + '0', code)
        if node.right:
            get_code(node.right, prefix + '0', code)
            # node.right.assign_codes(prefix + '1', code)
    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    #           bits required          *        chars
    return math.ceil(math.log2(len(f)))*sum([i[1] for i in f.items()])

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # print(list(C.values()))
    count = 0
    # print(C)
    # print(f)
    for i in f.items():
        # print(i)
        count += i[1]*len(C.get(i[0]))
        # print(i[1])
        # print(len(C.get(i[0])))
    return count
    

f = get_frequencies('test.txt')
# print(f)
# # print(len(f))
# # print(f.keys())
# for i in f.items():
#     print(i)
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))

for char, encoding in C.items():
    print(f"Character: {char}, Encoding: {encoding}")