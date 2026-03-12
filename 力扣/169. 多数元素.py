"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""
def majorityElement(self, nums):
    num_dict={}
    for num in nums:
        num_dict[num]= num_dict.get(num,0)+1
        if  num_dict[num]>len(nums)/2:
            return num

    # 摩根投票
    # candidate = None
    # count = 0
    #
    # for num in nums:
    #     if count == 0:
    #         candidate = num
    #
    #     if num == candidate:
    #         count += 1
    #     else:
    #         count -= 1
    #
    # return candidate



