class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.terminal = False
        self.letters = [None for i in range(26)]

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        if word == "":
            return
        
        if not self.letters[ord(word[0]) - ord('a')]:
            self.letters[ord(word[0]) - ord('a')] = Trie()
            
        if len(word) == 1:
            self.letters[ord(word[0]) - ord('a')].terminal = True
            
        
        self.letters[ord(word[0]) - ord('a')].insert(word[1:])
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        if word == "" and self.terminal:
            return True
        
        if word == "" and not self.terminal:
            return False
        
        if not self.letters[ord(word[0]) - ord('a')]:
            return False
        
        return self.letters[ord(word[0]) - ord('a')].search(word[1:])
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        if prefix == "":
            return True
        
        if not self.letters[ord(prefix[0]) - ord('a')]:
            return False
        
        return self.letters[ord(prefix[0]) - ord('a')].startsWith(prefix[1:])