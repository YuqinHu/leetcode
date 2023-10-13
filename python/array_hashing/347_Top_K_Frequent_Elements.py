def isValidSudoku(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num, c in count.items():
        freq[c].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res


