class Trinode(object):
    def __init__(self):
        self.children={}
        self.endofword= False
class Trie(object):

    def __init__(self):
        self.root= Trinode()

    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= Trinode()
            cur=cur.children[c]
        cur.endofword= True
        

    def search(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.endofword
        

    def startsWith(self, prefix):
        cur= self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)