class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, v in count.items():
            buckets[v].append(key)
        
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result