"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""


def merge(self, nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    n_p =0
    for i in range(len (nums1)):
        if i +1 > m:
            nums1[i]=nums2[n_p]
            n_p +=1
    # print(nums1)
    nums1.sort()
    # print(nums1)



    # nums =  nums1[:m] + nums2[:n]
    # sorted_nums1 = sorted(nums)
    # nums1 = sorted_nums1
    return nums1


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(merge(0,nums1, m, nums2, n))


