class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.max_val = 0
        self.lazy = 0

class SegmentTree:
    def __init__(self):
        self.low = 0
        self.high = 10 ** 9 - 1
        self.root = Node()
    
    def propagateDown(self, node):
        if node.lazy:
            if not node.left:
                node.left = Node()
            if not node.right:
                node.right = Node()
            
            node.left.max_val += node.lazy
            node.left.lazy += node.lazy

            node.right.max_val += node.lazy
            node.right.lazy += node.lazy

            node.lazy = 0
    
    def updateTree(self, node, l, r, start, end):
        if start > r or end < l:
            return
        
        if start <= l and r <= end:
            node.max_val += 1
            node.lazy += 1
            return
    
        self.propagateDown(node)

        mid = (l + r) // 2

        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()

        self.updateTree(node.left, l, mid, start, end)
        self.updateTree(node.right, mid + 1, r, start, end)

        node.max_val = max(node.left.max_val, node.right.max_val)
    
    # commented out the below method since it is unused for this part
    # def rangeQuery(self, node, l, r, start, end):
    #     if not node:
    #         return 0
        
    #     if start > r or end < l:
    #         return 0
        
    #     if start <= l and r <= end:
    #         return node.max_val
        
    #     self.propagateDown(node)

    #     mid = (l + r) // 2

    #     return max(self.rangeQuery(node.left, l, mid, start, end), self.rangeQuery(node.right, mid + 1, r, start, end))


class MyCalendarThree:

    def __init__(self):
        self.segmentTree = SegmentTree()

    def book(self, startTime: int, endTime: int) -> int:
                    
        self.segmentTree.updateTree(self.segmentTree.root, self.segmentTree.low, self.segmentTree.high, startTime, endTime - 1)
        return self.segmentTree.root.max_val
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)