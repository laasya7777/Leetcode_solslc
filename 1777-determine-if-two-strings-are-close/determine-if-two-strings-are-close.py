class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
      
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        
        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1
        
        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1
        
        
        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False
        
       
        freq1_sorted = []
        freq2_sorted = []
        
        for f in freq1:
            if f > 0:
                freq1_sorted.append(f)
        
        for f in freq2:
            if f > 0:
                freq2_sorted.append(f)
        
        freq1_sorted.sort()
        freq2_sorted.sort()
        
        return freq1_sorted == freq2_sorted
