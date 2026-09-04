class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isend = True

    def dfs(self,curr,i, word):
        if i == len(word):
            return curr.isend
        if word[i] in curr.children:
            return self.dfs(curr.children[word[i]],i+1,word)
        if word[i] == '.':
            for child in curr.children.values():
                if self.dfs(child,i+1,word):
                    return True
            return False
        return False

        
    def search(self, word: str) -> bool:
        return self.dfs(self.root,0,word)
