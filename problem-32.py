from unittest import result


class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        result = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                result.append([num_map[complement], i])
            num_map[num] = i
        return result

print(input(int(Solution().twoSum([2, 9, 7, 11, 17, 15], 26)))