/**

360. Sliding Window Median
https://www.lintcode.com/problem/sliding-window-median/description

**/
public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer
     * @return: The median of the element inside the window at each moving
     */
    public List<Integer> medianSlidingWindow(int[] nums, int k) {
        // write your code here

        if (nums == null || nums.length == 0) {
            return new ArrayList<Integer>();
        }

        int n = nums.length;
        PriorityQueue<Integer> max_queue = new PriorityQueue(n, Collections.reverseOrder());
        PriorityQueue<Integer> min_queue = new PriorityQueue(n);

        List<Integer> results = new ArrayList<Integer>();

        int right = 0;
        for (int left = 0; left < n; ++left) {
            while (right < n && right - left < k) {
                if (max_queue.size() == 0 || nums[right] <= max_queue.peek()) {
                    max_queue.offer(nums[right]);
                } else {
                    min_queue.offer(nums[right]);
                }
                balance(max_queue, min_queue);
                ++right;
            }
            if (right - left == k) {
                results.add(max_queue.peek());
            }
            if (right >= n) {
                break;  //because even if right == n, the result is already added in previous statement
            }

            if (nums[left] <= max_queue.peek()){
                max_queue.remove(nums[left]);
            } else {
                min_queue.remove(nums[left]);
            }
            balance(max_queue, min_queue);
        }
        return results;
    }

    private void balance(PriorityQueue<Integer> max_queue, PriorityQueue<Integer> min_queue) {
        while (max_queue.size() < min_queue.size()) {
            max_queue.offer(min_queue.poll());
        }
        while (max_queue.size() - min_queue.size() > 1) {
            min_queue.offer(max_queue.poll());
        }
    }
}
