import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int people_num = people.length;
        
        Arrays.sort(people);

        int i = 0;
        int j = people_num - 1;
        
        while (i <= j) {
            int weight = people[i] + people[j];
            
            if (weight > limit) {
                j--;
            } else {
                i++;
                j--;
            }
            
            answer++;
        }
        
        return answer;
    }
}