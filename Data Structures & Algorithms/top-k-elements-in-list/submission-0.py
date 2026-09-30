class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        target = sorted(freq.values(), reverse=True)[:k]
        result = []
        for key, value in freq.items():
            if value in target:
                result.append(key)

        return result