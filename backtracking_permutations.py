"""
回溯算法详解：以LeetCode全排列问题为例

回溯模板
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""

from typing import List

def permute_backtrack(nums: List[int]) -> List[List[int]]:
    """
    使用回溯算法解决全排列问题
    
    回溯算法核心思想：
    1. 选择：从可选列表中做出选择
    2. 约束：检查当前选择是否满足约束条件
    3. 目标：检查是否达到目标状态
    
    对于全排列问题：
    - 选择：每次从未选择的数字中选择一个
    - 约束：每个数字只能使用一次
    - 目标：形成一个完整的排列（长度等于原数组）
    """
    result = []  # 存储所有可能的排列
    path = []    # 当前正在构建的排列
    used = [False] * len(nums)  # 标记数字是否已被使用
    
    def backtrack():
        # 递归终止条件：当前路径长度等于数组长度
        if len(path) == len(nums):
            # 将当前路径的副本添加到结果中
            # 注意：必须是副本，因为path在后续会被修改
            result.append(path[:])  # 或者 path.copy()
            return
        
        # 遍历所有可能的选择
        for i in range(len(nums)):
            # 约束条件：如果数字已被使用，则跳过
            if used[i]:
                continue
            
            # 做选择：将数字添加到当前路径中
            path.append(nums[i])
            used[i] = True
            
            # 进入下一层决策树
            backtrack()
            
            # 撤销选择：回溯到上一状态
            path.pop()
            used[i] = False
    
    # 从空路径开始回溯
    backtrack()
    return result

def permute_backtrack_optimized(nums: List[int]) -> List[List[int]]:
    """
    优化版本的回溯算法实现
    """
    result = []
    
    def backtrack(start: int):
        # 当start等于数组长度时，说明已经形成一个完整排列
        if start == len(nums):
            result.append(nums[:])  # 添加当前排列的副本
            return
        
        # 从start位置开始尝试所有可能的交换
        for i in range(start, len(nums)):
            # 交换元素
            nums[start], nums[i] = nums[i], nums[start]
            
            # 递归处理下一个位置
            backtrack(start + 1)
            
            # 回溯：撤销交换
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result

# 演示回溯过程的详细版本
def permute_with_trace(nums: List[int]) -> List[List[int]]:
    """
    带有详细追踪信息的回溯算法实现
    """
    result = []
    path = []
    used = [False] * len(nums)
    indent = 0  # 用于显示递归层级
    
    def backtrack():
        nonlocal indent
        space = "  " * indent
        print(f"{space}进入递归层 {indent}: 当前路径 {path}")
        
        # 递归终止条件
        if len(path) == len(nums):
            print(f"{space}找到排列: {path}")
            result.append(path[:])
            return
        
        # 尝试所有可能的选择
        for i in range(len(nums)):
            if used[i]:
                continue
            
            # 做选择
            print(f"{space}选择数字 {nums[i]} (索引 {i})")
            path.append(nums[i])
            used[i] = True
            indent += 1
            
            # 递归
            backtrack()
            
            # 撤销选择
            indent -= 1
            path.pop()
            used[i] = False
            print(f"{space}撤销选择 {nums[i]} (索引 {i}), 当前路径 {path}")
    
    print(f"开始生成数组 {nums} 的全排列:")
    backtrack()
    return result

# 测试代码
if __name__ == "__main__":
    # 测试基本回溯算法
    nums = [1, 2, 3]
    print("=== 基本回溯算法 ===")
    result1 = permute_backtrack(nums)
    print(f"数组 {nums} 的全排列:")
    for i, perm in enumerate(result1):
        print(f"{i+1}. {perm}")
    
    print("\n=== 优化回溯算法 ===")
    result2 = permute_backtrack_optimized(nums.copy())  # 使用副本避免影响原数组
    print(f"数组 {nums} 的全排列 (优化版):")
    for i, perm in enumerate(result2):
        print(f"{i+1}. {perm}")
        
    print("\n=== 带追踪信息的回溯算法 ===")
    result3 = permute_with_trace([1, 2, 3])