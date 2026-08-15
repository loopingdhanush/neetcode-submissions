class Tries:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class PrefixTree:

    def __init__(self):
        self.root = Tries()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Tries()
            cur = cur.children[c]
        cur.endOfword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        