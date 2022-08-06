"""
170. Two Sum III - Data structure design

insertion - o(1)
find - o(n)
"""

class TwoSum:

    def __init__(self):
        self.storage = []

    def add(self, number: int) -> None:
        self.storage.append(number)
        

    def find(self, value: int) -> bool:
        missing_term = set()
        
        for num in self.storage:
            if num in missing_term:
                return True
            missing_term.add(value - num)
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)