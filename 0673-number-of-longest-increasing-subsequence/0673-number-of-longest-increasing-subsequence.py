class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [1] * n  # lengths[i] stores the length of the longest increasing subsequence ending at index i
        counts = [1] * n   # counts[i] stores the count of the longest increasing subsequences ending at index i

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        result = sum(count for length, count in zip(lengths, counts) if length == max_length)
        return result