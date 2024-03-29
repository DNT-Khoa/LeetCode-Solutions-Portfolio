class Solution {
    public int largestAltitude(int[] gain) {
        int maxAlt = 0;
        int sum = 0;
        
        for (int i = 0; i < gain.length; i++) {
            sum += gain[i];
            if (sum > maxAlt) {
                maxAlt = sum;
            }
        }
        
        return maxAlt;
    }
}