"""
1514. Robot Room Cleaner
https://www.lintcode.com/problem/robot-room-cleaner/
"""
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
DIRECTIONS  = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
    ]
class Solution:
    """
    :type robot: Robot
    :rtype: None
    """
    def cleanRoom(self, robot):
        #write your code here
        self.dfs(robot, 0, 0, 0, set())

    def dfs(self, robot, x, y, next_direction, visited):
        if (x, y) in visited:
            return
        visited.add((x, y))
        robot.clean()

        for _ in range(4):
            next_x, next_y = x + DIRECTIONS[next_direction][0], y + DIRECTIONS[next_direction][1]
            if robot.move():
                self.dfs(robot, next_x, next_y, next_direction, visited) #keep moving forward until obstacle
                self.backtrack(robot)
            robot.turnRight()
            next_direction = (next_direction + 1) % 4


    def backtrack(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
