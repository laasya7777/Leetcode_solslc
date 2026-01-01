class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                backtrack(path + [nums[i]])
                used[i] = False

        backtrack([])
        return res
