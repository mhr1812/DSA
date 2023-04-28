class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # (1) Helper function to check if two strings are similar
        def similar(a: str, b: str):
            # Indices of different letters
            diff1 = -1
            diff2 = -1

            for i in range(len(a)):
                if a[i] != b[i]:
                    if diff1 == -1:
                        diff1 = i
                    elif diff2 == -1:
                        diff2 = i
                    else:
                        # A third difference has been found
                        return False

            # We know there are exactly 0 or 2 differences now since a and b
            # are defined by the problem to be anagrams
            return True
        
        # List of groups (2D List of Lists of strings)
        groupList = []

        # (2) Iterate through input list of strings
        for s in strs:
            # Variable for group assignment of s
            foundGroup = -1

            for i, group in enumerate(groupList):
                # (3) Iterate through groups to search for similar strings to s
                for s2 in group:
                    if similar(s, s2):
                        # (4) We've found our first similar string
                        if foundGroup == -1:
                            # Assign s to group i
                            foundGroup = i
                            groupList[i].append(s)
                            break
                        # (5) We've found another similar string
                        else:
                            # Combine group foundGroup and group i
                            groupList[foundGroup] = groupList[foundGroup] + groupList[i]
                            del groupList[i]
                            break

            # (6) No similar string found in groups, add new group
            if foundGroup == -1:
                groupList.append([s])

        # (7) Profit
        return len(groupList)