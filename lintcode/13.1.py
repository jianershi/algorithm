class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    """
    2个循环，外面的循环source,内部循环target。要是不符合就break,要是内部循环完成就表示找到了。遍历了所有要是没有就不存在
    """
    def strStr(self, source, target):
        #异常检测
        if not target:
            return 0
        if len(target) > len(source):
            return -1

        # Write your code here
        for index in range(len(source)):
            ptr = 0
            while ptr < len(target) and index + ptr < len(source):
                if target[ptr] != source[index + ptr]:
                    break
                ptr += 1
                if ptr == len(target):
                    return index

        return -1


def main():
    s = Solution()
    print (s.strStr("abcdg","cdg"))

if __name__ == "__main__":
    main()
