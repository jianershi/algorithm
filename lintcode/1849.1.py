"""
1849. Grumpy Bookstore Owner
https://www.lintcode.com/problem/grumpy-bookstore-owner/description
"""
class Mood:
    GRUMPY = 1
    HAPPY = 0

class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """
    def maxSatisfied(self, customers, grumpy, X):
        # write your code here
        if not customers or not grumpy:
            return 0
        if X >= len(customers):
            return sum(customers)

        total_good_review_count = 0
        n = len(customers)

        window_bad_review_sum = 0
        for i in range(X):
            if grumpy[i] == Mood.GRUMPY:
                window_bad_review_sum += customers[i]
            if grumpy[i] == Mood.HAPPY:
                total_good_review_count += customers[i]

        max_bad_reviews = window_bad_review_sum

        left, right = 1, X
        while right < n:
            if grumpy[right] == Mood.GRUMPY:
                window_bad_review_sum += customers[right]
            if grumpy[right] == Mood.HAPPY:
                total_good_review_count += customers[right]
            if grumpy[left - 1] == Mood.GRUMPY:
                window_bad_review_sum -= customers[left - 1]
            max_bad_reviews = max(max_bad_reviews, window_bad_review_sum)

            left += 1
            right += 1
        return total_good_review_count + max_bad_reviews
