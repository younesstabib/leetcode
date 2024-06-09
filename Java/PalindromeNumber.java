class Solution {
    public boolean isPalindrome(int x) {
        if( x < 0){
            return false;
        }

        int original = x;
        int inverse = 0;

        while (x != 0) {
            inverse = inverse * 10 + x % 10;
            x /= 10;
        }

        return original == inverse;
    }
}