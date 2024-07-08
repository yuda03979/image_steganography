
class HuffmanNode:
    def __init__(self, letter, key:int):
        self.letter = letter # can be None or str
        self.key = key
        self.children = [None, None]

    def __repr__(self):
        return f'<HuffmanNode letter={self.letter} key={self.key}>'

    def set_right_child(self, child):
        self.children[1] = child # type(child) = HuffmanNode

    def set_left_child(self, child):
        self.children[0] = child # type(child) = HuffmanNode

    def get_right_child(self):
        return self.children[1]

    def get_left_child(self):
        return self.children[0]

    def __lt__(self, other):
        return True if self.key < other.key else False

    def __le__(self, other):
        return True if self.key <= other.key else False

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __ge__(self, other):
        return True if self.key >= other.key else False

    def __gt__(self, other):
        return True if self.key > other.key else False