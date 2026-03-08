class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda w: (-len(w), w))

        def is_subsequence(w):
            m = len(w)
            j = 0

            for ch in s:
                if j == m:
                    return True

                if w[j] == ch:
                    j += 1

            return j == m

        for word in dictionary:
            if is_subsequence(word):
                return word
        return ""