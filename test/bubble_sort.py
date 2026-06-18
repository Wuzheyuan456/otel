"""
冒泡排序 (Bubble Sort)
=====================
时间复杂度:
  最好: O(n)   — 数组已有序，加入提前退出优化后只需一趟
  平均: O(n²)
  最坏: O(n²)  — 数组完全逆序
空间复杂度: O(1) — 原地排序
稳定性: 稳定（相等元素不交换，相对顺序不变）

实现模型: claude-sonnet-4-6
"""


def bubble_sort(arr: list, reverse: bool = False) -> list:
    """
    冒泡排序：反复比较相邻元素，将较大（或较小）的元素逐步"冒泡"到末尾。

    每一趟遍历至少将一个元素放到最终位置，共需 n-1 趟。
    加入 swapped 标志：若某趟没有发生任何交换，说明已有序，提前退出。

    :param arr:     待排序列表（不修改原列表，返回新列表）
    :param reverse: True 表示降序，False 表示升序（默认）
    :return:        排序后的新列表
    """
    result = arr[:]          # 复制，不破坏原数组
    n = len(result)

    for i in range(n - 1):
        swapped = False      # 本趟是否发生了交换

        # 每趟结束后，末尾 i 个元素已就位，无需再比较
        for j in range(n - 1 - i):
            # 升序：左边 > 右边则交换；降序：左边 < 右边则交换
            should_swap = result[j] > result[j + 1] if not reverse else result[j] < result[j + 1]
            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # 本趟无交换，数组已有序，提前退出
        if not swapped:
            break

    return result


if __name__ == '__main__':
    test_cases = [
        ("空列表",       []),
        ("单元素",       [42]),
        ("已升序",       [1, 2, 3, 4, 5]),
        ("已降序",       [5, 4, 3, 2, 1]),
        ("随机数组",     [64, 34, 25, 12, 22, 11, 90]),
        ("含重复元素",   [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("降序排列测试", [3, 1, 4, 1, 5]),
    ]

    print("=" * 50)
    print("冒泡排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        if name == "降序排列测试":
            result = bubble_sort(data, reverse=True)
            print(f"{name}: {data} -> {result} (降序)")
        else:
            result = bubble_sort(data)
            print(f"{name}: {data} -> {result}")
