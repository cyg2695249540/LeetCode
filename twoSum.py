# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : twoSum.py
# @Author   : Pluto.
# @Time     : 2020/10/16 12:08
"""
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    #暴力枚举，时间复杂度O(N^2),空间复杂度O(1)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []

    #哈希表，时间复杂度O(N),空间复杂度O(N)
    def twoSum2(self,nums:List[int],target:int) ->List[int]:
        dic={}
        for k,v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v],k]
            dic[v]=k

if __name__ == '__main__':
    nums = [1,2, 7, 11, 15]
    target = 9
    if not isinstance(nums, List):
        raise TypeError("nums is not list")
    if not isinstance(target, int):
        raise TypeError("nums is not list")
    # ex=Solution().twoSum1(nums,target)
    ex=Solution().twoSum2(nums,target)
    print(ex)
