# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概述

Python 学习仓库，包含两类独立项目：
- **排序算法**：8 种经典排序算法的纯 Python 实现，每个算法单独一个文件
- **小游戏**：终端交互游戏（curses 库）

## 运行

```bash
# 排序算法（每个文件自带测试用例）
python bubble_sort.py

# 贪吃蛇（需要真实终端，不能在管道/IDE 内嵌终端中运行）
python snake_game.py
```

## 排序算法文件规范

每个算法文件遵循统一结构，新增时须保持一致：

1. **模块文档字符串**：时间复杂度（最好/平均/最坏）、空间复杂度、稳定性、`实现模型: <model>`
2. **实现函数**：接受 `arr: list` 和可选 `reverse: bool = False`，不修改原数组（先 `arr[:]` 复制），返回新列表
3. **`__main__` 测试块**：覆盖空列表、单元素、已升序、已降序、含重复元素、降序排列 6 类边界情况

## 已实现的算法

| 文件 | 算法 | 稳定性 | 平均时间复杂度 |
|------|------|--------|---------------|
| `bubble_sort.py` | 冒泡排序 | 稳定 | O(n²) |
| `selection_sort.py` | 选择排序 | 不稳定 | O(n²) |
| `insertion_sort.py` | 插入排序 | 稳定 | O(n²) |
| `shell_sort.py` | 希尔排序 | 不稳定 | O(n log n) |
| `merge_sort.py` | 归并排序 | 稳定 | O(n log n) |
| `quick_sort.py` | 快速排序 | 不稳定 | O(n log n) |
| `heap_sort.py` | 堆排序 | 不稳定 | O(n log n) |
| `counting_sort.py` | 计数排序（仅整数）| 稳定 | O(n + k) |

## 游戏文件

| 文件 | 描述 |
|------|------|
| `snake_game.py` | 贪吃蛇（curses），WASD/方向键控制，P 暂停，R 重开，Q 退出 |

## 环境配置

Claude Code 通过 ADVibe MaaS 平台接入，配置说明见 `setup-claude-code.md`。
