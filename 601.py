"""
601. Flatten 2D Vector
https://www.lintcode.com/problem/flatten-2d-vector/
九章强化班C9
"""
class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.i = 0
        self.j = -1

    # @return {int} a next element
    def next(self):
        # Write your code here
        ret = self.vec2d[self.i][self.j]
        return ret
        
    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        self.j += 1
        while self.i < len(self.vec2d) and self.j > len(self.vec2d[self.i]) - 1:
            self.i += 1
            self.j = 0
        
        return self.i < len(self.vec2d)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

