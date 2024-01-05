class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        
        String[] used = new String[words.length];
        int usedSize = 0;
        int breakIdx = -1;
        char prev = words[0].charAt(0);
        
        for (int i = 0; i < words.length; i++) {
            boolean flag = false;
            
            for (int j = 0; j < usedSize; j++) {
                if (words[i].equals(used[j])) {
                    flag = true;
                    break;
                }
            }
            
            if (flag || words[i].charAt(0) != prev) {
                breakIdx = i;
                break;
            } else {
                used[usedSize++] = words[i];
                prev = words[i].charAt(words[i].length() - 1);
            }
        }
        
        System.out.println(breakIdx);
        answer[0] = breakIdx % n + 1;
        
        if (breakIdx != - 1) {
            answer[1] = breakIdx / n + 1;
        }

        return answer;
    }
}