/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */
public class InvertedIndex {

    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            StringTokenizer tokenizer = new StringTokenizer(value.content);
            while (tokenizer.hasMoreTokens()) {
                output.collect(tokenizer.nextToken(), value.id);
            }

        }
    }

    public static class Reduce {
        public void reduce(String key, Iterator<Integer> values,
                           OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            List<Integer> result = new ArrayList<Integer>();
            int last_element = -1;
            while (values.hasNext()) {
                Integer now = values.next();
                if (now != last_element) {
                    result.add(now);
                    last_element = now;
                }

            }
            output.collect(key, result);
        }
    }
}
