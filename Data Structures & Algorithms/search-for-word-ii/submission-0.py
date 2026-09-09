class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = word
    def findWords(self, board, words):
        for word in words:
            self.insert(word)
        res = []
        def backtrack(row,col,node):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return 
            
            char = board[row][col]
            if char == 'Y':
                return 
            
            if char not in node.children:
                return 
            
            nextnode = node.children[char]
            if nextnode.word:
                res.append(nextnode.word)
                nextnode.word = None
            temp = board[row][col]
            board[row][col] = 'Y'
            backtrack(row-1,col,nextnode) 
            backtrack(row,col+1,nextnode) 
            backtrack(row+1,col,nextnode)
            backtrack(row,col-1,nextnode)
            board[row][col] = temp

        for row in range(len(board)):
            for col in range(len(board[0])):
                backtrack(row, col, self.root)

        return res
        

board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]
sol = Solution()
print(sol.findWords(board,words))