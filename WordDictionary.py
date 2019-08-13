class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.terminal = False
        self.letters = [None for i in range(26)]
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        
        if word == "":
            return
        
        if not self.letters[ord(word[0]) - ord('a')]:
            self.letters[ord(word[0]) - ord('a')] = WordDictionary()
            
        if len(word) == 1:
            self.letters[ord(word[0]) - ord('a')].terminal = True
            
        self.letters[ord(word[0]) - ord('a')].addWord(word[1:])
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        if word == "" and self.terminal:
            return True
        
        if word == "" and not self.terminal:
            return False
        
        
        if word[0] != '.':
            if self.letters[ord(word[0]) - ord('a')]:
                return self.letters[ord(word[0]) - ord('a')].search(word[1:])
        
            else:
                return False
            
        else:
            for i in range(26):
                if self.letters[i]:
                    if self.letters[i].search(word[1:]):
                        return True
                    
            return False