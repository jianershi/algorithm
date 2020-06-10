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
class Pair implements Comparator<Pair>, Comparable<Pair> {
    public int count;
    public String content;
    public Pair(String content, Integer count){
        this.count = count;
        this.content = content;
    }
    public int compare(Pair a, Pair b) {
        if (a.count != b.count) {
            return (a.count - b.count);
        }
        return b.content.compareTo(a.content);
    }
    public int compareTo(Pair b){
        return compare(this, b);
    }
}



public class TopKFrequentWords {

    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            StringTokenizer tokenizer = new StringTokenizer(value.content);
            while (tokenizer.hasMoreTokens()) {
                output.collect(tokenizer.nextToken(), 1);
            }
        }
    }

    public static class Reduce {

        private int k;
        private PriorityQueue<Pair> queue;

        public void setup(int k) {
            // initialize your data structure here
            this.k = k;
            queue = new PriorityQueue<Pair>(k);
        }

        public void reduce(String key, Iterator<Integer> values) {
            // Write your code here
            int count = 0;
            while (values.hasNext()){
                count += values.next();
            }
            Pair current = new Pair(key, count);
            if (queue.size() < k) {
                queue.add(current);
            } else {
                Pair head = queue.peek();
                // PairComparator<Pair> com = new PairComparator()
                if (current.compareTo(head) > 0) {
                    queue.poll();
                    queue.add(current);
                }
            }
        }

        public void cleanup(OutputCollector<String, Integer> output) {
            // Output the top k pairs <word, times> into output buffer.
            // Ps. output.collect(String key, Integer value);
            List<Pair> results = new ArrayList<Pair>();
            while (!queue.isEmpty()) {
                results.add(queue.poll());
            }
            for (int i = results.size() - 1; i >= 0; --i) {
                Pair pair = results.get(i);
                output.collect(pair.content, pair.count);
            }
        }
    }
}
