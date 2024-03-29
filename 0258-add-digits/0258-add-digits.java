class Solution {
    public int addDigits(int num) {
        
        while (num / 10 != 0) {
            int sum = 0;
            
            while (num != 0) {
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num;
        
        // This is solution with O(1) time complexity
        // if (num <= 9) {
        //     return num;
        // }
        // if (num % 9 == 0) {
        //     return 9;
        // }
        // return num % 9;
    }
}