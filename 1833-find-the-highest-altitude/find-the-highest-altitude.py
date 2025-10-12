class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        initial_alt=[0]
        for i in gain:
            initial_alt.append(i+initial_alt[-1])
        return max(initial_alt)
        
        