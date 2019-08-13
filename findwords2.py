# time limit exceeded didn't feel like working on this more
# 34/36 test cases passed

class TrieNode(object):
    def __init__(self):
        self.terminal = False
        self.letters = [None for i in range(26)]

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        node = TrieNode()
        for word in words:
            if not node.letters[ord(word[0]) - ord('a')]:
                node.letters[ord(word[0]) - ord('a')] = TrieNode()
        
            if len(word) == 1:
                node.letters[ord(word[0]) - ord('a')].terminal = True
        
            self.initialize(node.letters[ord(word[0]) - ord('a')], word[1:])
            
        outputWords = []
            
        visited = [[False for j in range(len(board[i]))] for i in range(len(board))]
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                for word in words:
                    if node.letters[ord(board[i][j]) - ord('a')] != None:
                        if self.dfs(i, j, board, node, visited, word) and word not in outputWords:
                            outputWords.append(word)

        return outputWords
        
    def initialize(self, node, word):
        if word == "":
            return
        
        if not node.letters[ord(word[0]) - ord('a')]:
            node.letters[ord(word[0]) - ord('a')] = TrieNode()
        
        if len(word) == 1:
            node.letters[ord(word[0]) - ord('a')].terminal = True
            
        self.initialize(node.letters[ord(word[0]) - ord('a')], word[1:])
        
        
    def dfs(self, i, j, board, node, visited, word):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        
        if visited[i][j]:
            return False
        
        if word == "" or (len(word) == 1 and board[i][j] == word[0]):
            return True
        
        if board[i][j] != word[0] or node == None:
            return False
        
        visited[i][j] = True
        valid = self.dfs(i - 1, j, board, node.letters[ord(word[0]) - ord('a')], visited, word[1:]) or \
            self.dfs(i + 1, j, board, node.letters[ord(word[0]) - ord('a')], visited, word[1:]) or \
            self.dfs(i, j - 1, board, node.letters[ord(word[0]) - ord('a')], visited, word[1:]) or \
            self.dfs(i, j + 1, board, node.letters[ord(word[0]) - ord('a')], visited, word[1:])
            
        visited[i][j] = False
        return valid