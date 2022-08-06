"""
170. Two Sum III - Data structure design

insertion - o(n)
find - o(1)
"""

class TwoSum:

    def __init__(self):
        self.storage = []
        self.possible_sum = set()
        

    def add(self, number: int) -> None:
        for num in self.storage:
            self.possible_sum.add(num + number)
        self.storage.append(number)

    def find(self, value: int) -> bool:
        return value in self.possible_sum
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)