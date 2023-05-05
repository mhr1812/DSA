class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #vowels  = {'a','e','i','o','u'}
        n,curr = len(s),0
        for i in range(k):
            if s[i] in {'a','e','i','o','u'}:
                curr+=1
        ans = curr
        for i in range(n-k):
            if s[i] in {'a','e','i','o','u'}:
                curr-=1
            if s[i+k] in {'a','e','i','o','u'}:
                curr+=1
            #curr = curr-old+new
            ans = max(ans,curr)
        return ans