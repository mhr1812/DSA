class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [0 for i in range(n)]
        # c = Counter(nums)  
        # d = {}    
        # for i in range(n):
        #     if nums[i] not in d:
        #         d[nums[i]] = i
        #     else:
        #         d[nums[i]] += i
        # for i in range(n):
        #     a[i] = d[nums[i]]-c[nums[i]]*i
        #     d[nums[i]]-=2*i
        #     c[nums[i]]-=2
        d = defaultdict(list)
        for i in range(n):
            d[nums[i]].append(i)
        for num,val in d.items():
            suffixSum=sum(val)
            preffixSum=0
            s=len(val)
            p=0
            for i in val:
                preffixSum+=i
                p+=1
                suffixSum-=i
                s-=1
                a[i]=-preffixSum + p*i - s*i + suffixSum
        return a    
        return a
                