# coding:utf-8
import random


def quicksort(nums):
    """リストの数でpivotの値より
    小さいものを左、大きいものを右に集めて2つのリストで返す"""
    numlen = len(nums)
    if numlen <= 1:
        return nums
    elif numlen == 2:
        if nums[0] > nums[1]:
            return [nums[1], nums[0]]
        else:
            return nums
    # pivotを選ぶ
    pivotindex = random.randint(0, len(nums)-1)
    pivot = nums.pop(pivotindex)
    nums = nums+[pivot]
    # 左マーカを右に動かしてpivot以上の数にたどり着いた場合Stop
    Rstart = numlen-1
    for Lmarker in range(numlen-1):
        pivot = nums[-1]
        Lnum = nums[Lmarker]
        if Lnum >= pivot:
            for Rmarker in range(Rstart, -1, -1):
                Rnum = nums[Rmarker]
                if Rmarker == Lmarker:
                    nums[Rmarker], nums[-1] = nums[-1], nums[Rmarker]
                    return quicksort(nums[:Rmarker])+[nums[Rmarker]]+quicksort(nums[Rmarker+1:])
                elif Rnum < pivot:
                    Rstart = Rmarker
                    nums[Rmarker], nums[Lmarker] = nums[Lmarker], nums[Rmarker]
                    break
    return quicksort(nums[:-1])+[nums[-1]]


before = [5, 2, 1, 7, 4, 56, 3, 5, 10, 55, 34, 100, 342, 152, 2]
print(f'before {before}')
after = quicksort(before)
print(f'after {after}')
