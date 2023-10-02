class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c = defaultdict(int)
        for x,t in groupby(colors):
            c[x]+=max(len(list(t))-2,0)
        if c['A']>c['B']:
            return True
        return False
        