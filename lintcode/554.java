/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 */
public class SortIntegers {

    public static class Map {
        public void map(int _, List<Integer> value,
                        OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            // for (int i = 0; i < value.size(); ++i) {
            Collections.sort(value);
            output.collect("key", value);
            // }
        }
    }

    public static class Reduce {
        public void reduce(String key, List<List<Integer>> values,
                           OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
            // for (int i = 0; i < values.size(); ++i) {
                // queue.add(values[i])
            // }

            for (List<Integer> list: values) {
                for (Integer i: list) {
                    queue.add(i);
                }
            }
            List<Integer> list = new ArrayList<Integer>();
            while (!queue.isEmpty()){
                list.add(queue.poll());
            }
            output.collect("key", list);
        }
    }
}   
