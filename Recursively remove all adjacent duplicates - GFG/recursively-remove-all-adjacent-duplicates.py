#User function Template for python3

class Solution:
    def rremove (self, S):
		#code here
		a = list(S)
		st = []
		i,n = 0,len(S)
		while i<n:
		    if st and st[-1]==S[i]:
		        while i<n and S[i]==st[-1]:
		            i+=1
		        st.pop()
		    if i<n:
		        st.append(S[i])
		        i+=1
		if a==st:
		    return ''.join(a)
		else:
		    return self.rremove(''.join(st))
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends