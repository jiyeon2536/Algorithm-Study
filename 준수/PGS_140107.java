import java.lang.Math;

class Solution {
    public long solution(int k, long d) {
        long answer = 0;
        
        for (long i = 0; i <= d; i += k) {
            int res = (int) Math.sqrt(d * d - i * i);
            answer += res / k + 1;
        }
        
        return answer;
    }
}