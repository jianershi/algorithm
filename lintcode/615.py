from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        # pre_dict = self.build_dict(numCourses, prerequisites)
        # in_degree = self.get_indegree(pre_dict)
        pre_dict, in_degree = self.build_dict_and_indegrees(numCourses, prerequisites)

        order = 0
        queue = deque([i for i in in_degree if in_degree[i] == 0]) #put all indegree = 0 item into queue

        while (queue):
            node = queue.popleft()
            order += 1
            for neibour in pre_dict[node]:
                in_degree[neibour] -= 1
                if in_degree[neibour] == 0:
                    queue.append(neibour)
        return order == numCourses

    def build_dict_and_indegrees(self, numCourses, prerequisites):
        pre_dict = {x: [] for x in range(numCourses)}
        in_degrees = {x: 0 for x in range(numCourses)}
        for neibour, out_node in prerequisites:
            pre_dict[out_node].append(neibour)
            in_degrees[neibour] += 1
        return pre_dict, in_degrees

def main():
    s = Solution()
    print(s.canFinish(10,[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]))

if __name__ == "__main__":
    main()
