class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      
        if len(word1) != len(word2):
            return False
        
        
        chars1 = set(word1)
        chars2 = set(word2)
        if chars1 != chars2:
            return False
        
        freqs1 = [word1.count(c) for c in chars1]
        freqs2 = [word2.count(c) for c in chars1]  
        return sorted(freqs1) == sorted(freqs2)
