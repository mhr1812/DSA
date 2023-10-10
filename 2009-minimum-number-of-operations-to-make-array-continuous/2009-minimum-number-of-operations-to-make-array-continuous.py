sys.stdout = open('user.out', 'w')
nums = None
for line in map(loads, stdin):
    if isinstance(line, list):
        nums = line
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0
        
        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1
            
            count = j - i
            ans = min(ans, n - count)

        print(ans)
        nums = None