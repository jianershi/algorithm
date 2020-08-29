/**
489. Robot Room Cleaner
https://leetcode.com/problems/robot-room-cleaner/
1514. Robot Room Cleaner
https://www.lintcode.com/problem/robot-room-cleaner/description
**/

/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
    int delta_x[4] = {-1, 0, 1, 0};
    int delta_y[4] = {0, 1, 0, -1};
public:
    void cleanRoom(Robot& robot) {
        set<pair<int, int>> v;
        v.insert(make_pair(0,0));
        dfs(robot, 0, 0, v, 0);  
    }
    
    void dfs(Robot& robot, int x, int y, set<pair<int, int>> &v, int dir) {
        robot.clean();
        
        for (int i = 0; i < 4; ++i) {
            int nx = x + delta_x[(dir + i) % 4];
            int ny = y + delta_y[(dir + i) % 4];
            if (v.count(make_pair(nx, ny))) {
                robot.turnRight(); 
                continue;
            }
            v.insert(make_pair(nx, ny));
            if (robot.move()) {
                dfs(robot, nx, ny, v, (dir + i) % 4);
                backTrack(robot);
            }
            robot.turnRight();
        }
    }
    void backTrack(Robot& robot) {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }
};