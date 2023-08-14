class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums[:k]
        heapq.heapify(arr)
        for num in nums[k:]:
            if num>arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr,num)
        return arr[0]
        
            