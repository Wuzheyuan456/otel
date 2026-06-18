"""
插入排序 (Insertion Sort)
=========================
时间复杂度:
  最好: O(n)   — 数组已有序，每个元素只需比较一次
  平均: O(n²)
  最坏: O(n²)  — 数组完全逆序，每个元素需比较到最前端
空间复杂度: O(1) — 原地排序
稳定性: 稳定（插入时遇到相等元素停在其右侧，不改变相对顺序）

适用场景: 小规模数据或近乎有序的数据，实际常数因子小，效率较高

实现模型: claude-sonnet-4-6
"""


def insertion_sort(arr: list, reverse: bool = False) -> list:
    """
    插入排序：将数组分为"已排序"和"未排序"两部分。
    初始已排序部分只包含第一个元素，每次从未排序部分取出第一个元素，
    在已排序部分从右向左扫描，找到合适位置插入。

    类比：整理扑克牌——每拿到一张新牌，将它插入手中已排好的牌的正确位置。

    :param arr:     待排序列表（不修改原列表）
    :param reverse: True 表示降序，False 表示升序（默认）
    :return:        排序后的新列表
    """
    result = arr[:]
    n = len(result)

    for i in range(1, n):
        key = result[i]   # 当前待插入的元素
        j = i - 1         # 从已排序部分的末尾开始向左扫描

        # 将比 key 大（升序）或小（降序）的元素右移一位，为 key 腾出位置
        if not reverse:
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
        else:
            while j >= 0 and result[j] < key:
                result[j + 1] = result[j]
                j -= 1

        result[j + 1] = key  # 将 key 放到正确位置

    return result


if __name__ == '__main__':
    test_cases = [
        ("空列表",       []),
        ("单元素",       [42]),
        ("已升序",       [1, 2, 3, 4, 5]),
        ("已降序",       [5, 4, 3, 2, 1]),
        ("随机数组",     [5, 2, 4, 6, 1, 3]),
        ("含重复元素",   [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("降序排列测试", [3, 1, 4, 1, 5]),
    ]

    print("=" * 50)
    print("插入排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        if name == "降序排列测试":
            result = insertion_sort(data, reverse=True)
            print(f"{name}: {data} -> {result} (降序)")
        else:
            result = insertion_sort(data)
            print(f"{name}: {data} -> {result}")
