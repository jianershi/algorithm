from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = deque([start])
        visited = set([start])
        length = 0

        while (queue):
            node = queue.popleft()
            length += 1
            print ("{}:{}".format(node, length))
            if node == end:
                return length
            for next_word in self.next_word(node):
                if next_word in dict and next_word not in visited:
                    queue.append(next_word)
                    visited.add(next_word)

        return -1

    def next_word(self, word):
        word_list = set()
        for i in range(len(word)):
            left = word[:i]
            center = word[i]
            right = word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char != center:
                    word_list.add(left + char + right)
        # print ("length: {}: {}".format(len(word_list), word_list))
        return word_list

def main():
    s = Solution()
    print (s.ladderLength("hit", "cog", {"hot","dot","dog","lot","log"}))

if __name__ == "__main__":
    main()
