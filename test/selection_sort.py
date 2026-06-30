"""
选择排序 (Selection Sort)
=========================
时间复杂度:
  最好: O(n²) — 无论输入状态，始终需要完整扫描未排序部分
  平均: O(n²)
  最坏: O(n²)
空间复杂度: O(1) — 原地排序
稳定性: 不稳定（将最小值换到前面时，可能跳过相等元素）

特点: 交换次数最少（最多 n-1 次），适合交换代价很高的场景

实现模型: claude-sonnet-4-6
"""


def selection_sort(arr: list, reverse: bool = False) -> list:
    """
    选择排序：将数组分为"已排序"和"未排序"两部分。
    每一趟从未排序部分找出最小值（升序）或最大值（降序），
    将其与未排序部分的第一个元素交换，从而扩大已排序区域。

    类比：每次从一堆扑克牌中挑出最小的放到已排好的位置末尾。

    :param arr:     待排序列表（不修改原列表）
    :param reverse: True 表示降序，False 表示升序（默认）
    :return:        排序后的新列表
    """
    result = arr[:]
    n = len(result)

    for i in range(n - 1):
        # 在未排序部分 [i, n) 中找极值的下标
        extreme_idx = i
        for j in range(i + 1, n):
            if not reverse:
                if result[j] < result[extreme_idx]:  # 寻找最小值
                    extreme_idx = j
            else:
                if result[j] > result[extreme_idx]:  # 寻找最大值
                    extreme_idx = j

        # 将极值交换到未排序部分的起始位置（若已在该位置则无需交换）
        if extreme_idx != i:
            result[i], result[extreme_idx] = result[extreme_idx], result[i]

    return result


if __name__ == '__main__':
    test_cases = [
        ("空列表",       []),
        ("单元素",       [42]),
        ("已升序",       [1, 2, 3, 4, 5]),
        ("已降序",       [5, 4, 3, 2, 1]),
        ("随机数组",     [64, 25, 12, 22, 11]),
        ("含重复元素",   [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("降序排列测试", [3, 1, 4, 1, 5]),
    ]

    print("=" * 50)
    print("选择排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        if name == "降序排列测试":
            result = selection_sort(data, reverse=True)
            print(f"{name}: {data} -> {result} (降序)")
        else:
            result = selection_sort(data)
            print(f"{name}: {data} -> {result}")
