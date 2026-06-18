"""
希尔排序 (Shell Sort)
=====================
时间复杂度:
  最好: O(n log n) — 取决于间距序列
  平均: O(n log² n) — 使用 Knuth 序列时的经验值
  最坏: O(n²)       — 使用 Shell 原始序列（gap = n/2）时
空间复杂度: O(1) — 原地排序
稳定性: 不稳定（跨间距的交换可能打乱相等元素的顺序）

核心思想: 插入排序的改进版。先用较大间距对数组进行粗略排序，
使元素能快速移动到大致正确的位置；间距逐渐缩小，最后间距为 1
时退化为普通插入排序，但此时数组已近乎有序，效率很高。

实现模型: claude-sonnet-4-6
"""


def _generate_knuth_gaps(n: int) -> list:
    """
    生成 Knuth 间距序列：h = 1, 4, 13, 40, 121, ...
    公式: h = 3 * h + 1，取所有小于 n//3 的值，从大到小返回。
    Knuth 序列比 Shell 原始序列（n/2, n/4, ...）性能更好。
    """
    gaps = []
    h = 1
    while h < n // 3:
        gaps.append(h)
        h = 3 * h + 1
    return gaps[::-1]  # 从大到小


def shell_sort(arr: list) -> list:
    """
    希尔排序：使用 Knuth 间距序列，对每个间距执行插入排序。

    外层循环遍历间距序列（从大到小）；
    对于每个间距 gap，将数组看成 gap 个独立的子序列，
    对每个子序列执行插入排序。

    :param arr: 待排序列表（不修改原列表）
    :return:    升序排列的新列表
    """
    result = arr[:]
    n = len(result)

    if n <= 1:
        return result

    gaps = _generate_knuth_gaps(n)
    if not gaps:
        gaps = [1]  # 至少用间距 1（退化为插入排序）

    for gap in gaps:
        # 对间距为 gap 的子序列执行插入排序
        for i in range(gap, n):
            temp = result[i]   # 当前待插入元素
            j = i

            # 在间距为 gap 的已排序子序列中找插入位置
            while j >= gap and result[j - gap] > temp:
                result[j] = result[j - gap]  # 右移 gap 位
                j -= gap

            result[j] = temp   # 插入到正确位置

    return result


if __name__ == '__main__':
    test_cases = [
        ("空列表",     []),
        ("单元素",     [42]),
        ("两元素",     [2, 1]),
        ("已升序",     [1, 2, 3, 4, 5]),
        ("已降序",     [5, 4, 3, 2, 1]),
        ("随机数组",   [8, 3, 7, 1, 5, 9, 2, 6, 4]),
        ("含重复元素", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("大规模测试", list(range(50, 0, -1))),
    ]

    print("=" * 50)
    print("希尔排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        result = shell_sort(data)
        display = result if len(result) <= 15 else f"{result[:5]} ... {result[-5:]} (共{len(result)}个)"
        input_display = data if len(data) <= 15 else f"{data[:5]}... (共{len(data)}个)"
        print(f"{name}: {input_display} -> {display}")
