"""
815. Course Schedule IV
https://www.lintcode.com/problem/course-schedule-iv/description?_from=ladder&&fromId=160
DFS
"""
class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        # Write your code here

        map = self.build_map(n, p)
        in_degrees = self.build_indegree(map)
        visited = set()

        total_ways = [0]
        self.dfs(n, map, in_degrees, 0, total_ways, visited)
        return total_ways[0]

    def build_map(self, n, p): #prerequisite->course
        map = {x:set() for x in range(n)}
        for course, prerequisite in p:
            map[prerequisite].add(course)
        return map

    def build_indegree(self, map):
        in_degrees = {x:0 for x in map}
        for course, prerequisites in map.items():
            for neighbour in prerequisites:
                in_degrees[neighbour] = in_degrees.get(neighbour, 0) + 1
        return in_degrees

    def dfs(self, n, map, in_degrees, course_count, total_ways, visited):
        if course_count == n:
            total_ways[0] += 1
            return

        for node in in_degrees:
            if node in visited:
                continue
            if in_degrees[node] == 0:
                visited.add(node)
                for neighbour in map[node]:
                    in_degrees[neighbour] -= 1

                self.dfs(n, map, in_degrees, course_count + 1, total_ways, visited)
                
                for neighbour in map[node]:
                    in_degrees[neighbour] += 1
                visited.remove(node)
