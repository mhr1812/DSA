class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for d,a in sorted(tickets,reverse=True):
            graph[d].append(a)
        st = ["JFK"]
        ans = []
        while st:
            if graph[st[-1]]:
                st.append(graph[st[-1]].pop())
            else:
                ans.append(st.pop())
        return ans[::-1]