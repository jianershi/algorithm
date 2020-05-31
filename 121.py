from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here

        distance = {}
        dict.append(start)
        dict.append(end)
        self.bfs(end, start, dict, distance, 0)
        print (distance)
        results = []
        self.dfs(start, end, dict, distance, [start], results)
        print (results)
        return results

    def bfs(self, root, target, dict, distance, total_distance):
        queue = deque([root])
        # visited = set([root])
        distance[start] = 0
        while queue:
            total_distance += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                # distance[node] = total_distance
                for word in self.next_word(node):
                    if word in dict and word not in distance:
                        queue.append(word)
                        distance[word] = distance[node] + 1


    def dfs(self, start, target, dict, distance, path, results):
        if target == start:
            results.append(list(path))
            return

        for word in self.next_word(start):
            if word in dict and distance[word] < distance[start]:
                path.append(word)
                self.dfs(word, target, dict, distance, path, results)
                path.pop()


    def next_word(self, curr):
        word_list = set()
        for index in range(len(curr)):
            left = curr[:index]
            center = curr[index]
            right = curr[index + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if center != c:
                    word_list.add("".join([left, c, right]))
        # print (word_list)
        return word_list

def main():
    s = Solution()
    s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])

if __name__=="__main__":
    main()
