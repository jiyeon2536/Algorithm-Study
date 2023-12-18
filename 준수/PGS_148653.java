class Solution {
    public int solution(int storey) {
        int answer = 0;
        int temp = storey; 
        int size = 0;
        int prev = 0;

        while (temp > 0) {
            int now = temp % 10;
            
            if (now > 5) {
                temp += 10;
                answer += 10 - now;
            } else if (now < 5) {
                answer += now;
            } else if (now == 5) {
                answer += now;
                
                if (temp / 10 > 0 && temp % 100 >= 50) {
                    temp += 10;
                }
            }
            
            answer += prev;
            
            temp /= 10;
        }
        
        return answer;
    }
}