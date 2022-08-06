"""
170. Two Sum III - Data structure design

insertion - o(1)
find - o(nlogn)
"""

class TwoSum:

    def __init__(self):
        self.stack = []
        

    def add(self, number: int) -> None:
        self.stack.append(number)
        

    def find(self, value: int) -> bool:
        self.stack.sort()
        
        left, right = 0, len(self.stack) - 1
        while left < right:
            if self.stack[left] + self.stack[right] < value:
                left += 1
            elif self.stack[left] + self.stack[right] > value:
                right -= 1
            else:
                return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)value)