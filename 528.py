"""
528. Flatten Nested List Iterator
https://www.lintcode.com/problem/flatten-nested-list-iterator/description
九章算法强化班C7

大部分计算得在hasNext里就处理掉。因为万一遇到[[],[]]，如果不在hasNext里面处理掉。就会造成外部函数调用
hasNext -> 回答 yes
然后去掉 next -> None 的情况。
所以处理必须得在hasNext里面处理掉。
"""
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        # self.stack = []
        # if nestedList.isInteger():
        #     self.stack.append(nestedList.getInteger())
        # else:
        #     self.stack.extend(nestedList.getList()[::-1])
        self.stack = nestedList[::-1]

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(self.stack.pop().getList()[::-1])
        return len(self.stack) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())