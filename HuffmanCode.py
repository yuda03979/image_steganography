from BinaryHeap import *
from HuffmanNode import *
from Functions import *

class HuffmanCode:
    """
    HuffmanCode class is used to generate Huffman code.
    it returns dict: {letterA: HuffmanCode, letterB: HuffmanCode}
    """
    def __init__(self, ascii_text:str):
        self.ascii_text = ascii_text
        self.dict_ascii_bin = dict()
        self.dict_bin_ascii = dict()
        self.bin_text = ""

    # operations:

        self.huffman_node_array = self.counting()
        # after building self.huffman_node_array, it will make it a heap
        self.heap = BinaryHeap()
        self.heap.build_heap(self.huffman_node_array)
        # initialize the root of the "huffman tree"
        self.tree_root = self.encode_tree()
        # decoding the tree:
        self.decode_tree(self.tree_root, "")
        # writing the bin_text
        self.bin_text = translate_ascii_to_bin(self.ascii_text, self.dict_ascii_bin)


    def counting(self):
        # !!! can use collection.Counter
        count_letter = dict()
        for i in self.ascii_text:
            if i in count_letter:
                count_letter[i] += 1
            else:
                count_letter[i] = 1


        huffman_node_array = []
        for i in count_letter:
            huffman_node_array.append(HuffmanNode(i, count_letter[i]))
        return huffman_node_array

    def encode_tree(self):
        """
        bulding the tree for huffman code.
        :return: HuffmanNode, that is the root of the tree.
        """
        while self.heap.get_size() > 1:
            min1 = self.heap.dequeue()
            min2 = self.heap.dequeue()
            node = HuffmanNode(None, min1.key + min2.key)
            node.set_right_child(min1)
            node.set_left_child(min2)
            self.heap.enqueue(node)

        return self.heap.dequeue()


    def decode_tree(self, node:HuffmanNode, huffman_code:str):
        """
        make the self.dict_ascii_bin, that hold for each letter the huffman code
        :param node: HuffmanNode
        :param huffman_code: e.g. 011
        """
        if node.letter is not None:
            self.dict_ascii_bin[node.letter] = huffman_code
            self.dict_bin_ascii[huffman_code] = node.letter
        else:
            if node.get_left_child() is not None:
                self.decode_tree(node.get_left_child(), huffman_code + "1")
            if node.get_right_child() is not None:
                self.decode_tree(node.get_right_child(), huffman_code + "0")
    def get_ascii_text(self):
        return self.ascii_text

    def get_bin_text(self):
        return self.bin_text

    def get_dict_ascii_bin(self):
        return self.dict_ascii_bin

    def get_dict_bin_ascii(self):
        return self.dict_bin_ascii