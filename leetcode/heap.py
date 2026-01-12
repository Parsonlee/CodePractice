# 堆（Heap）概念与要点（简洁版）：

# 定义：堆是一棵满足“堆性质”的完全二叉树。常见有两种：
# 最大堆（max-heap）：每个父节点 >= 子节点，根为最大值。
# 最小堆（min-heap）：每个父节点 <= 子节点，根为最小值。

# 存储：通常用数组表示（紧凑、连续），节点索引从0开始时：
# 父节点索引 parent(i) = (i - 1) // 2
# 左子节点 index = 2i + 1，右子节点 index = 2i + 2

# 核心操作（复杂度）：
# push/insert：把元素放在数组末尾，向上调整（sift-up），O(log n)
# pop/remove root（取最大或最小）：用末尾元素覆盖根，弹出末尾，向下调整（sift-down），O(log n)
# heapify（把任意数组变成堆）：从底向上对非叶节点做sift-down，O(n)
# top/peek：查看根元素，O(1)

# 用途：优先队列、选择问题（如第k大）、流式数据维护top-k、堆排序等。


class MinHeap:
    """
    最小堆实现类
    堆顶元素始终是最小值
    """
    def __init__(self, data=None):
        """
        初始化最小堆
        :param data: 可选的初始数据列表
        """
        # 如果提供了初始数据，则复制一份；否则创建空列表
        self.a = data[:] if data else []
        # 如果有初始数据，则将其转换为堆结构
        if self.a:
            self._heapify()

    def _swap(self, i, j):
        """
        交换数组中两个位置的元素
        :param i: 第一个元素的索引
        :param j: 第二个元素的索引
        """
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def _sift_up(self, idx):
        """
        向上调整堆结构（上浮操作）
        用于插入新元素时维护堆性质
        :param idx: 需要上浮的元素索引
        """
        # 新插入元素从idx向上移动，保证父<=子
        while idx > 0:
            # 计算父节点索引: (idx-1)//2
            p = (idx - 1) // 2
            # 如果父节点值小于等于当前节点值，则满足堆性质，停止上浮
            if self.a[p] <= self.a[idx]:
                break
            # 否则交换父节点和当前节点
            self._swap(p, idx)
            # 继续向上检查
            idx = p

    def _sift_down(self, idx):
        """
        向下调整堆结构（下沉操作）
        用于删除堆顶元素时维护堆性质
        :param idx: 需要下沉的元素索引
        """
        n = len(self.a)
        while True:
            # 计算左右子节点索引
            left = 2 * idx + 1
            right = left + 1
            # 假设当前节点就是最小的
            smallest = idx
            
            # 检查左子节点是否存在且比当前最小节点更小
            if left < n and self.a[left] < self.a[smallest]:
                smallest = left
                
            # 检查右子节点是否存在且比当前最小节点更小
            if right < n and self.a[right] < self.a[smallest]:
                smallest = right
                
            # 如果最小节点仍是原节点，说明已满足堆性质，停止下沉
            if smallest == idx:
                break
                
            # 否则交换当前节点与最小节点
            self._swap(idx, smallest)
            # 继续向下检查
            idx = smallest

    def push(self, val):
        """
        向堆中插入新元素
        :param val: 要插入的值
        """
        # 将新元素添加到数组末尾
        self.a.append(val)
        # 通过上浮操作维护堆性质
        self._sift_up(len(self.a) - 1)

    def pop(self):
        """
        弹出堆顶元素（最小值）
        :return: 堆顶元素
        :raises IndexError: 当堆为空时抛出异常
        """
        # 检查堆是否为空
        if not self.a:
            raise IndexError("pop from empty heap")

        # 保存堆顶元素作为返回值
        top = self.a[0]
        # 弹出数组最后一个元素
        last = self.a.pop()
        
        # 如果还有剩余元素
        if self.a:
            # 将最后一个元素移到堆顶
            self.a[0] = last
            # 通过下沉操作维护堆性质
            self._sift_down(0)
            
        return top

    def peek(self):
        """
        查看堆顶元素但不弹出
        :return: 堆顶元素，如果堆为空则返回None
        """
        return self.a[0] if self.a else None

    def _heapify(self):
        """
        将数组转换为堆结构
        从最后一个非叶子节点开始，自底向上进行下沉操作
        """
        # 从最后一个非叶子节点开始下沉
        n = len(self.a)
        # 最后一个非叶子节点的索引是 (n-2)//2
        for i in range((n - 2) // 2, -1, -1):
            self._sift_down(i)