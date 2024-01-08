import java.lang.Math;

class Solution {
    static int emoticonNum = 0;
    static int maxSigned = 0;
    static int maxPrice = 0;
    
    public void check(int[][] users, int[] discount, int[] emoticons) {
        int signed = 0;
        int price = 0;
        
        for (int[] user: users) {
            int emoticonPrice = 0;
            
            for (int i = 0; i < emoticonNum; i++) {
                if (discount[i] >= user[0]) { 
                    emoticonPrice += (emoticons[i] / 100) * (100 - discount[i]);
                    // System.out.println(emoticonPrice);
                }
            }
            
            if (emoticonPrice >= user[1]) {
                signed += 1;
            } else {
                price += emoticonPrice;
            }
        }
        
        if (signed > maxSigned) {
            maxSigned = signed;
            maxPrice = price;
        } else if (signed == maxSigned) {
            maxPrice = Math.max(maxPrice, price);
        }
    }
    
    public void comb(int[][] users, int[] discount, int idx, int[] emoticons) {
        if (idx == emoticonNum) {
            check(users, discount, emoticons);
            return;
        }
        
        for (int i = 1; i < 5; i++) {
            discount[idx] = i * 10;
            comb(users, discount, idx + 1, emoticons);
            discount[idx] = 0;
        }
    }
    
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = new int[2];
        
        emoticonNum = emoticons.length;
        
        // 할인율은 10, 20, 30, 40
        int[] discount = new int[emoticonNum];
        
        comb(users, discount, 0, emoticons);
        
        answer[0] = maxSigned;
        answer[1] = maxPrice;
        
        return answer;
    }
}