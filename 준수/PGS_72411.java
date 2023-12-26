import java.util.*;

class Solution {
    static ArrayList<Menu> combs = new ArrayList<>();
    
    class Menu {
        String comb;
        int orderNum;
        
        Menu(String comb) {
            this.comb = comb;
            this.orderNum = 1;
        }
    }
    
    public void dfs(String order, int idx, String res, int[] course) {
        if (idx == order.length()) {
            for (int num: course) {
                if (num == res.length()) {
                    for (int i = 0; i < combs.size(); i++) {
                        if (res.equals(combs.get(i).comb)) {
                            combs.get(i).orderNum++;
                            return;
                        }
                    }
                    
                    Menu menu = new Menu(res);
                    combs.add(menu);
                }
            }
            return;
        }
        
        dfs(order, idx + 1, res + order.charAt(idx), course);
        dfs(order, idx + 1, res, course);
    }
    
    class MenuComparator implements Comparator<Menu> {
        @Override
        public int compare(Menu o1, Menu o2) {
            return o2.orderNum - o1.orderNum;
        } 
    }
    
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        
        for (String order: orders) {
            char[] temp = order.toCharArray();
            Arrays.sort(temp);
            order = new String(temp);
            dfs(order, 0, "", course);
        }
        
        Collections.sort(combs, new MenuComparator());
        
        int[] max_cnt = new int[11];
        
        ArrayList<String> result = new ArrayList<>();
        
        for (int i = 0; i < combs.size(); i++) {
            Menu comb = combs.get(i);
            
            if (comb.orderNum > 1 && max_cnt[comb.comb.length()] <= comb.orderNum) {
                max_cnt[comb.comb.length()] = comb.orderNum;
                result.add(comb.comb);
            }
        }
        
        Collections.sort(result);

        answer = new String[result.size()];
        
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
            System.out.println(answer[i]);
        }
        
        return answer;
    }
}