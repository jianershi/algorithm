/**
  81. Find Median from Data Stream
  https://www.lintcode.com/problem/find-median-from-data-stream/description
**/
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: the median of numbers
     */
    public int[] medianII(int[] nums) {
        // write your code here
        int n = nums.length;
        PriorityQueue<Integer> max_heap = new PriorityQueue<Integer>(n, Collections.reverseOrder());
        PriorityQueue<Integer> min_heap = new PriorityQueue<Integer>(n);

        int[] results = new int[n];
        for (int i = 0; i < n; ++i) {
            if (max_heap.size() == 0 || nums[i] <= max_heap.peek()) {
                max_heap.offer(nums[i]);
            } else {
                min_heap.offer(nums[i]);
            }
            balance(max_heap, min_heap);

            results[i] = max_heap.peek();
        }

        return results;
    }
    private void balance(PriorityQueue<Integer> max_heap, PriorityQueue<Integer> min_heap) {
        while (min_heap.size() > max_heap.size()) {
            max_heap.offer(min_heap.poll());
        }

        while (max_heap.size() > min_heap.size() + 1) {
            min_heap.offer(max_heap.poll());
        }
    }
}
