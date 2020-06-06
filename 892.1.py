import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        if not words:
            return ""

        n = len(words)
        graph = {}

        for word in words:
            for c in word:
                graph[c] = set()

        for i in range(len(words) - 1):
            if words[i].startswith(words[i + 1]) and len(words[i]) > len(words[i + 1]):
                return ""
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break

        in_orders = self.get_in_orders(graph)

        # print (in_orders, graph)
        heap = [node for node in in_orders if in_orders[node] == 0]
        heapq.heapify(heap)

        topological_order = ""

        while heap:
            head = heapq.heappop(heap)
            topological_order += head
            for neighbor in graph[head]:
                in_orders[neighbor] -= 1
                if in_orders[neighbor] == 0:
                    heapq.heappush(heap, neighbor)

        #check if there are circular dependency in graph
        if len(topological_order) == len(graph):
            return topological_order

        return ""

    def get_in_orders(self, graph):
        in_orders = {node: 0 for node in graph}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                in_orders[neighbor] += 1

        return in_orders


s = Solution()
words = ["wrt","wrf","er","ett","rftt"]
print(s.alienOrder(words))
