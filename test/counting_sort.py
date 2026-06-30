"""
计数排序 (Counting Sort)
========================
时间复杂度:
  最好: O(n + k)  — k 为数值范围（max - min + 1）
  平均: O(n + k)
  最坏: O(n + k)
空间复杂度: O(n + k) — 需要计数数组（大小 k）和输出数组（大小 n）
稳定性: 稳定（反向填充输出数组保证相等元素的相对顺序）

适用场景: 整数排序，且数值范围 k 不大（k 接近 n 时最优）
限制: 仅适用于整数（或可映射为整数的元素），k 过大时内存开销大

实现模型: claude-sonnet-4-6
"""


def counting_sort(arr: list) -> list:
    """
    计数排序（支持负整数）：
    1. 统计每个值出现的次数，存入计数数组
    2. 对计数数组做前缀和，得到每个值的最终位置
    3. 从右向左扫描原数组，按计数数组将元素放入正确位置（保证稳定性）

    处理负数：将所有值平移 -min_val，使最小值映射为 0。

    :param arr: 待排序整数列表（不修改原列表）
    :return:    升序排列的新列表
    :raises TypeError: 若包含非整数元素
    """
    if not arr:
        return []

    # 输入校验：只支持整数
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("计数排序仅支持整数列表")

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1  # 数值范围

    # 阶段1：统计每个值的出现次数（平移处理负数）
    count = [0] * k
    for val in arr:
        count[val - min_val] += 1

    # 阶段2：前缀和 — count[i] 表示值 <= (i + min_val) 的元素总数
    for i in range(1, k):
        count[i] += count[i - 1]

    # 阶段3：反向填充输出数组（从右到左保证稳定性）
    output = [0] * len(arr)
    for val in reversed(arr):
        idx = val - min_val
        count[idx] -= 1
        output[count[idx]] = val

    return output


if __name__ == '__main__':
    test_cases = [
        ("空列表",       []),
        ("单元素",       [42]),
        ("已升序",       [1, 2, 3, 4, 5]),
        ("已降序",       [5, 4, 3, 2, 1]),
        ("随机整数",     [4, 2, 2, 8, 3, 3, 1]),
        ("含负数",       [-3, 1, -1, 0, 2, -2, 3]),
        ("全相同元素",   [5, 5, 5, 5]),
        ("含重复元素",   [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]),
        ("大范围整数",   [100, 1, 50, 25, 75]),
    ]

    print("=" * 50)
    print("计数排序测试  |  模型: claude-sonnet-4-6")
    print("=" * 50)
    for name, data in test_cases:
        result = counting_sort(data)
        print(f"{name}: {data} -> {result}")

    # 测试异常处理
    print("\n异常测试:")
    try:
        counting_sort([1, 2.5, 3])
    except TypeError as e:
        print(f"含浮点数 -> 捕获异常: {e}")
