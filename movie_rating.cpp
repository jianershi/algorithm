/**
Movie Rating

defition:
dp[i][condition] : max sum can get from *previous* ith movies, when choose to SKIP/NOT_SKIP at ith step

function:
dp[i][SKIP] = dp[i - 1][NOT_SKIP]
dp[i][NOT_SKIP] = max(dp[i - 1][SKIP], dp[i - 1][NOT_SKIP]) + nums[i - 1]


initialization:
dp[0][NOT_SKIP] = 0
dp[0][SKIP] = 0

answer:
max(dp[n])

define:
1 not skipping
0 skip
**/
#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
public:
    int movieRating(std::vector<int> &ratings) {
        if (ratings.size() == 0) {
            return 0;
        }
        int n = ratings.size();
        std::vector<std::vector<int>> dp (n + 1, std::vector<int>(2, 0));

        for (int i = 1; i < n + 1; ++i) {
            dp[i][0] = dp[i - 1][1];
            dp[i][1] = std::max(dp[i - 1][0], dp[i - 1][1]) + ratings[i - 1];
        }
        
        return std::max(dp[n][0], dp[n][1]);

    }

};

int main() {
    Solution s;
    std::vector<int> ratings = {9, -1, -3, 4, 5};   
    std::cout << s.movieRating(ratings) << std::endl;
}
