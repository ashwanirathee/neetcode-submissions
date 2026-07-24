class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node(-1)

    def insert(self, word: str) -> None:
        curr = self.root
        for j in range(len(word)):
            print(curr.val)
            if word[j] not in curr.children:
                curr.children[word[j]] = Node(word[j])
            # curr.children[word[j]] = Node(word[j])
            curr = curr.children[word[j]]
        curr.is_word=True

    def search(self, word: str) -> bool:
        curr = self.root
        for j in range(len(word)):
            print(curr.val)
            if word[j] not in curr.children:
                return False
            curr = curr.children[word[j]]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for j in range(len(prefix)):
            print(curr.val)
            if prefix[j] not in curr.children:
                return False
            curr = curr.children[prefix[j]]
        return True
        
        