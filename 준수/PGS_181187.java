import java.lang.Math;

class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        long cnt = 0;
        
        for (long i = 1; i <= r2; i++) {
            int max_y = (int) Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2));
            int min_y = (int) Math.ceil(Math.sqrt(Math.pow(r1, 2) - Math.pow(i, 2)));
            answer += max_y - min_y + 1;
        }
        
        answer *= 4;
        
        return answer;
    }
}