"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""


def rotate(self, nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == '__main__':
    # removeDuplicates(nums
    rotate(0,nums = [1,2,3,4,5,6,7], k = 3)
    pass
