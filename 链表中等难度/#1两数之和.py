class Solution(object):
    # 解法一：暴力破解
    # 复杂度分析：时间复杂度：O(n^2)空间复杂度：O(1) -- 5s
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    # 解法二：哈希表，保持数组中每个元素和他下标对应的最好方法就是哈希表
    # 复杂度分析：时间复杂度：O(n)空间复杂度：O(n)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

        # enumerate:将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        # Python 2.3. 以上版本可用，2.6 添加 start 参数。
        # enumerate(sequence, [start=0])
        # sequence -- 一个序列、迭代器或其他支持迭代对象。
        # start -- 下标起始位置。


if __name__ == '__main__':
    nums = [0, 5, 4, 0]
    target = 0
    print(Solution().twoSum(nums, target))
