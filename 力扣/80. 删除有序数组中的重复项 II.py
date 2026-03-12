"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
def removeDuplicates(self, nums):
    oc_nums = 0
    num= nums[len(nums)-1]
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == num:
            oc_nums += 1
            if oc_nums >2:
                nums.pop(i)
        else:
            oc_nums=1
            num= nums[i]
    return len(nums)

if __name__ == '__main__':
    removeDuplicates(0,[1,1,1,2,2,3])
