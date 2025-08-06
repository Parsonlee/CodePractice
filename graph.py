"""
本模块实现了深度优先搜索（DFS）和广度优先搜索（BFS）算法，
用于在二维网格表示的图中进行遍历。

网格被假定为一个由列表组成的列表，其中1代表陆地，0代表水域。
"""

from collections import deque
from typing import List, Tuple


def dfs_recursive(grid: List[List[int]], row: int, col: int) -> None:
    """
    从(row, col)开始递归执行DFS。
    将访问过的陆地单元格标记为0以避免重复访问。

    参数:
        grid: 表示网格的二维列表。
        row: 起始行索引。
        col: 起始列索引。
    """
    # 检查越界或水域/已访问单元格
    if (
        row < 0
        or row >= len(grid)
        or col < 0
        or col >= len(grid[0])
        or grid[row][col] != 1
    ):
        return

    # 标记单元格为已访问
    grid[row][col] = 0

    # 探索邻居（上、下、左、右）
    dfs_recursive(grid, row - 1, col)  # 上
    dfs_recursive(grid, row + 1, col)  # 下
    dfs_recursive(grid, row, col - 1)  # 左
    dfs_recursive(grid, row, col + 1)  # 右


def dfs_iterative(grid: List[List[int]], start_row: int, start_col: int) -> None:
    """
    使用栈迭代执行DFS。
    将访问过的陆地单元格标记为0以避免重复访问。

    参数:
        grid: 表示网格的二维列表。
        start_row: 起始行索引。
        start_col: 起始列索引。
    """
    stack = [(start_row, start_col)]

    while stack:
        row, col = stack.pop()

        # 检查越界或水域/已访问单元格
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] != 1
        ):
            continue

        # 标记单元格为已访问
        grid[row][col] = 0

        # 将邻居添加到栈中（顺序可能影响遍历）
        stack.append((row - 1, col))  # 上
        stack.append((row + 1, col))  # 下
        stack.append((row, col - 1))  # 左
        stack.append((row, col + 1))  # 右


def bfs_iterative(grid: List[List[int]], start_row: int, start_col: int) -> None:
    """
    使用队列迭代执行BFS。
    将访问过的陆地单元格标记为0以避免重复访问。

    参数:
        grid: 表示网格的二维列表。
        start_row: 起始行索引。
        start_col: 起始列索引。
    """
    queue = deque([(start_row, start_col)])

    while queue:
        row, col = queue.popleft()

        # 检查越界或水域/已访问单元格
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] != 1
        ):
            continue

        # 标记单元格为已访问
        grid[row][col] = 0

        # 将邻居添加到队列中
        queue.append((row - 1, col))  # 上
        queue.append((row + 1, col))  # 下
        queue.append((row, col - 1))  # 左
        queue.append((row, col + 1))  # 右


def count_islands(grid: List[List[int]], method: str = "dfs_recursive") -> int:
    """
    使用指定的搜索方法计算网格中的岛屿数量。

    参数:
        grid: 表示网格的二维列表。
        method: 要使用的搜索方法('dfs_recursive', 'dfs_iterative', 'bfs_iterative')。

    返回:
        岛屿的数量。
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    # 创建网格副本以避免修改原始网格
    grid_copy = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == 1:
                # 发现一个岛屿，执行搜索以标记所有连接的陆地
                dfs_recursive(grid_copy, r, c)
                # dfs_iterative(grid_copy, r, c)
                # bfs_iterative(grid_copy, r, c)

                island_count += 1

    return island_count


# 示例用法（注释掉以供模块使用）：
# grid_example = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1]
# ]
# print("岛屿数量 (DFS 递归):", count_islands(grid_example, 'dfs_recursive'))
# print("岛屿数量 (DFS 迭代):", count_islands(grid_example, 'dfs_iterative'))
# print("岛屿数量 (BFS 迭代):", count_islands(grid_example, 'bfs_iterative'))
