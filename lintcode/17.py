class Solution:
    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(list(S))
            return

        S.append(nums[index])
        print ("index = %d, nums[%d] = %d, S = %s, results = %s" % (index, index, nums[index], S, self.results))
        self.search(nums, S, index + 1)
        print ("index = %d, nums[%d] = %d, S = %s, results = %s" % (index, index, nums[index], S, self.results))
        S.pop()
        print ("index = %d, nums[%d] = %d, S = %s, results = %s" % (index, index, nums[index], S, self.results))
        self.search(nums, S, index + 1)
        print ("index = %d, nums[%d] = %d, S = %s, results = %s" % (index, index, nums[index], S, self.results))

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results

def main():
    s = Solution()
    print (s.subsets([1,2]))

if __name__=="__main__":
    main()
