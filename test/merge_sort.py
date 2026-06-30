"""
归并排序 (Merge Sort)
=====================
时间复杂度:
  最好: O(n log n)
  平均: O(n log n)
  最坏: O(n log n) — 所有情况均一致，性能稳定
空间复杂度: O(n) — 合并时需要额外数组存放临时结果
稳定性: 稳定（合并时左半优先，相等元素保持原顺序）

实现模型: claude-sonnet-4-6
"""


def _merge(left: list, right: list) -> list:
    """
    合并两个已有序的子数组为一个有序数组。

    双指针分别扫描 left 和 right：
    - 取较小的元素放入结果
    - 某一侧扫描完后，将另一侧剩余元素直接追加
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # 稳定性关键：相等时优先取左侧元素
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 追加未扫描完的部分
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: list) -> list:
    """
    归并排序（递归分治）：
    1. 将数组从中间一分为二
    2. 递归地对左右两半分别排序
    3. 将两个有序子数组合并为一个有序数组

    :param arr: 待排序列表
    :return:    排序后的新列表（不修改原列表）
    """
    # 基准情况：空数组或单元素，已天然有序
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])   # 递归排左半
    right_sorted = merge_sort(arr[mid:])  # 递归排右半

    return _merge(left_sorted, right_sorted)


if __name__ == '__main__':
    test_cases = [
        ("空列表",     []),
        ("单元素",     [42]),
        ("已升序",     [1, 2, 3, 4, 5]),
        ("已降序",     [5, 4, 3, 2, 1]),
        ("随机数组",   [38, 27, 43, 3, 9, 82, 10]),
        ("含重复元素", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("两元素",     [2, 1]),
    ]

    print("=" * 50)
    print("归并排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        result = merge_sort(data)
        print(f"{name}: {data} -> {result}")
