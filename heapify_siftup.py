import sys
import collections
class Solution:
    # @param A: Given an integer array
    # @return: void
    def  siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            temp = A[k]
            A[k] = A[father]
            A[father] = temp

            k = father
    def heapify(self, A):
        for i in range(len(A) - 1, -1, -1):
            self.siftup(A, i)

def main():
    s = Solution()
    A = [3,2,1,4,5]
    original = A.copy()
    s.heapify(A)
    print ("Original: %s, Heapified: %s" % (original,A))

if __name__ == "__main__":
    main()
