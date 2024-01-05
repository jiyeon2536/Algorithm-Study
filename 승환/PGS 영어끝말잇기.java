import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {};
        answer = new int[2];
        answer[0] = 0;
        answer[1] = 0;
        Map<String, Integer> map = new HashMap<>(words.length);
        // 한글자인 단어이거나
        // 앞 사람이 말한 단어의 마지막 문자로 시작하는 단어가 아니거나
        // 이미 말했던 단어라면 stop!
        int cnt = 0;
        String temp = "";
        for(int i=0; i < words.length; i++){
            if(i >= 1){
            }
            if (map.containsKey(words[i]) || words[i].length() == 1 || 
                i >= 1 && !words[i].substring(0, 1).
                equals(words[i-1].substring(words[i-1].length() - 1)))
            {
                answer[0] = i % n + 1;
                answer[1] = (i + n)/ n;
                break;
            } else {
                map.put(words[i], 1);
            }
        }
        return answer;
    }
}
