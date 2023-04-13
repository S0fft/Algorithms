class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        nums = [str(x) for x in nums]
        result = 0

        for x in nums:
            if len(x) % 2 == 0:
                result += 1

        return result


class Solution:
    def sumOfUnique(self, nums: list[int]):
        result = []
        for x in nums:
            if not nums.count(x) >= 2:
                result.append(x)

        return sum(result)
