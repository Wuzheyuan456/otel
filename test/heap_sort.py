"""
堆排序 (Heap Sort)
==================
时间复杂度:
  最好: O(n log n)
  平均: O(n log n)
  最坏: O(n log n) — 所有情况一致
空间复杂度: O(1) — 原地排序，仅用常数额外空间
稳定性: 不稳定（堆调整过程中可能打乱相等元素的顺序）

实现模型: claude-sonnet-4-6
"""


def _heapify(arr: list, n: int, root: int) -> None:
    """
    下沉（sift-down）操作：将以 root 为根的子树调整为最大堆。

    假设 root 的左右子树已经满足最大堆性质，
    将 root 与其最大子节点比较，若小于子节点则交换并继续向下调整。

    在数组中，下标 i 的节点：
      左子节点下标: 2*i + 1
      右子节点下标: 2*i + 2

    :param arr:  数组
    :param n:    堆的有效大小（排序过程中逐渐缩小）
    :param root: 当前需要调整的根节点下标
    """
    largest = root       # 假设根节点最大
    left = 2 * root + 1
    right = 2 * root + 2

    # 与左子节点比较
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 与右子节点比较
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 若根节点不是最大值，则交换并继续下沉
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, n, largest)


def heap_sort(arr: list) -> list:
    """
    堆排序分两个阶段：
    1. 建堆（Build Max-Heap）：从最后一个非叶节点开始向上逐一 heapify，
       时间 O(n)。
    2. 排序：反复将堆顶（最大值）与末尾元素交换，缩小堆范围后重新 heapify，
       时间 O(n log n)。

    :param arr: 待排序列表
    :return:    升序排列的新列表
    """
    result = arr[:]
    n = len(result)

    if n <= 1:
        return result

    # 阶段1：建最大堆
    # 最后一个非叶节点下标为 n//2 - 1
    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    # 阶段2：逐步将最大值放到末尾
    for i in range(n - 1, 0, -1):
        # 将当前最大值（堆顶）与末尾交换
        result[0], result[i] = result[i], result[0]
        # 对缩小后的堆重新堆化
        _heapify(result, i, 0)

    return result


if __name__ == '__main__':
    test_cases = [
        ("空列表",     []),
        ("单元素",     [42]),
        ("已升序",     [1, 2, 3, 4, 5]),
        ("已降序",     [5, 4, 3, 2, 1]),
        ("随机数组",   [12, 11, 13, 5, 6, 7]),
        ("含重复元素", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("两元素",     [2, 1]),
    ]

    print("=" * 50)
    print("堆排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        result = heap_sort(data)
        print(f"{name}: {data} -> {result}")
