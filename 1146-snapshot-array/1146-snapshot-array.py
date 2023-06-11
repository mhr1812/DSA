class SnapshotArray:

    def __init__(self, length: int):
        self.a = [[(0,0)] for i in range(length)]
        self.id = 0
        
    def set(self, index: int, val: int) -> None:
        self.a[index].append((self.id,val))

    def snap(self) -> int:
        self.id+=1
        return self.id-1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.a[index]
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid][0]<=snap_id:
                l = mid+1
            else:
                r = mid-1
        return arr[r][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)