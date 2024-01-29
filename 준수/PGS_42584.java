import java.util.*;

class Solution {
    class Data {
        int index;
        int price;
        
        Data(int index, int price) {
            this.index = index;
            this.price = price;
        }
    }
    
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        List<Data> stack = new ArrayList<>();
        
        stack.add(new Data(0, prices[0]));
        
        for (int i = 1; i < prices.length; i++) {
            Data data = new Data(i, prices[i]);
            
            while (!stack.isEmpty() && prices[i] < stack.get(stack.size() - 1).price) {
                int temp = stack.remove(stack.size() - 1).index;
                answer[temp] = i - temp;
            }
            
            stack.add(data);
        }
        
        while (!stack.isEmpty()) {
            int temp = stack.remove(stack.size() - 1).index;
            answer[temp] = prices.length - temp - 1;
        }
        
        return answer;
    }
}