import java.util.*;

class Solution {
    static int[] stack = new int[1000001];
    
    public String solution(String number, int k) {
        String answer = "";
        int len = number.length();
        int size = 0;
        int idx = 0;
        
        while (idx < len) {
            int temp = (int) number.charAt(idx) - (int) '0';
            
            if (size == 0) {
                stack[size++] = temp;
                idx++;
                continue;
            }
            
            while (k > 0 && size > 0 && stack[size - 1] < temp) {
                stack[size - 1] = 0;
                size--;
                k--;
            }
            
            stack[size++] = temp;
            idx++;
        }
        
        while (idx < len) {
            int temp = (int) number.charAt(idx++) - (int) '0';
            stack[size++] = temp;
        }
        
        for (int i = 0; i < size - k; i++) {
            answer += (char) (stack[i] + (int) '0');
        }
        
        return answer;
    }
}