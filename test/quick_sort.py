"""
快速排序 (Quick Sort)
=====================
时间复杂度:
  最好: O(n log n) — 每次 pivot 均匀分割数组
  平均: O(n log n)
  最坏: O(n²)      — 数组已有序且每次选首/末元素为 pivot
空间复杂度: O(log n) — 递归调用栈（平均），最坏 O(n)
稳定性: 不稳定（交换可能改变相等元素的相对顺序）

实现模型: claude-sonnet-4-6
"""
import random


def _partition(arr: list, low: int, high: int) -> int:
    """
    Lomuto 分区方案：
    1. 随机选取 pivot（减少最坏情况概率）并置于末尾
    2. i 指向"小于 pivot 区域"的最后一个位置
    3. 遍历 low..high-1，遇到 <= pivot 的元素就把它放到左区
    4. 最后将 pivot 放到正确位置并返回该下标
    """
    # 随机化 pivot，避免有序输入退化为 O(n²)
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

    pivot = arr[high]
    i = low - 1  # 小于 pivot 区域的右边界

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将 pivot 放到最终位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_recursive(arr: list, low: int, high: int) -> None:
    """递归快排：分区后对左右子数组分别递归。"""
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quick_sort_recursive(arr, low, pivot_idx - 1)   # 排左半部分
        _quick_sort_recursive(arr, pivot_idx + 1, high)  # 排右半部分


def quick_sort(arr: list) -> list:
    """
    快速排序入口：复制原数组后原地排序，返回新列表。

    :param arr: 待排序列表
    :return:    升序排列的新列表
    """
    result = arr[:]
    if len(result) > 1:
        _quick_sort_recursive(result, 0, len(result) - 1)
    return result


if __name__ == '__main__':
    test_cases = [
        ("空列表",     []),
        ("单元素",     [42]),
        ("已升序",     [1, 2, 3, 4, 5]),
        ("已降序",     [5, 4, 3, 2, 1]),
        ("随机数组",   [64, 34, 25, 12, 22, 11, 90]),
        ("含重复元素", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("大规模测试", list(range(100, 0, -1))),
    ]

    print("=" * 50)
    print("快速排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        result = quick_sort(data)
        display = result if len(result) <= 15 else f"{result[:5]} ... {result[-5:]} (共{len(result)}个)"
        print(f"{name}: {data[:10]}{'...' if len(data)>10 else ''} -> {display}")
