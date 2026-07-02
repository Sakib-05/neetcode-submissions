class PrefixTree:

    def __init__(self):
        self.root = {}
        print(self.root)
        

    def insert(self, word: str) -> None:
        if word[0] not in self.root:
            if len(word) ==1:
                self.root[word[0]] = TreeNode(True)
            else:
                self.root[word[0]] = TreeNode()

        node = self.root[word[0]]

        for i in range(1,len(word)):
            if i == len(word)-1:
                if word[i] not in node.children:
                    node.children[word[i]] = TreeNode(True)
                else:
                    node = node.children[word[i]]
                    node.end = True


            
            elif word[i] in node.children:
                node = node.children[word[i]]
            else:
                node.children[word[i]] = TreeNode()
                node = node.children[word[i]]




    def search(self, word: str) -> bool:
        if word[0] not in self.root:
            return False
        
        node = self.root[word[0]]

        for i in range(1, len(word)):
            char = word[i]

            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.root:
            return False

        node = self.root[prefix[0]]

        for i in range(1,len(prefix)):
            char = prefix[i]
            if char not in node.children:
                return False
            
            node = node.children[char]

        return True

class TreeNode:
    def __init__(self,end = False):
        self.children ={}
        self.end = end
        