import java.util.*;

class Solution {
    
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        ArrayList<String> arr = new ArrayList<String>();
        
        Arrays.sort(phone_book);
        
        for (int i = 0; i < phone_book.length - 1; i++) {
            if (!answer) break;
            String target = phone_book[i];
            
            for (int k = 0; k < target.length(); k++) {
                if (target.charAt(k) != phone_book[i + 1].charAt(k)) break;

                if (k == target.length() - 1) answer = false;
            }
        }
        
        return answer;
    }
}