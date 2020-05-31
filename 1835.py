class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        # write your code here
        memo =  {} # index, curr_step
        # print(memo)
        return self.dfs(steps, arrLen, 0, steps, memo)
      
    """
    return true if curr_step is 0 and back in origin
    return False otherwise
    recursively go to 3 directions that is within range, need to have counter.
    easisest way is to have global counter, but that is not very nice.
    but is the easiest way.
  
    divide and conquer, the total number of ways is the sum of ways of 3 directions.
  
    """
    def dfs(self, steps, arr_len, index, curr_step, memo):
        if not (0 <= index < arr_len):
            return 0
        if (index, curr_step) in memo:
            return memo[(index, curr_step)]
        if curr_step == 0:
            if index == 0:
                memo[(index, curr_step)] = 1
            else:
                memo[(index, curr_step)] = 0
            return memo[(index, curr_step)]
              
        left_total = self.dfs(steps, arr_len, index - 1, curr_step - 1, memo)
        right_total = self.dfs(steps, arr_len, index + 1, curr_step - 1, memo)
        center_total = self.dfs(steps, arr_len, index, curr_step - 1, memo)
        memo[(index, curr_step)] = left_total + right_total + center_total
        return memo[(index, curr_step)]
