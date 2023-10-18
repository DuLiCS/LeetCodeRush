public class L274 {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] buckets = new int[n + 1];

        for (int cite:citations) {
            if (cite > n){
                buckets[n] += 1;
            }
            else
            {
                buckets[cite] += 1;
            }
        }
        int sum = 0;
        for (int i = n; i >= 0 ; i--) {
            sum += buckets[i];
            if (sum >= i){
                return i;
            }
        }
        return 0;
    }
}
