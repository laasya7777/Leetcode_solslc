class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        base = sum(strategy[i] * prices[i] for i in range(n)) 
        orig = [strategy[i] * prices[i] for i in range(n)]    
        sellGain = [(1 - strategy[i]) * prices[i] for i in range(n)]

        prefixOrig = [0] * (n + 1)
        prefixSell = [0] * (n + 1)

        for i in range(n):
            prefixOrig[i + 1] = prefixOrig[i] + orig[i]
            prefixSell[i + 1] = prefixSell[i] + sellGain[i]

        bestGain = 0
        half = k // 2

        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            loss = prefixOrig[mid] - prefixOrig[l]
            gain = prefixSell[r] - prefixSell[mid]

            bestGain = max(bestGain, gain - loss)

        return base + max(0, bestGain)
