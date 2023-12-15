import java.util.*;

class Solution {
    class Plan {
        String name;
        int start;
        int playtime;
        
        Plan(String name, String start, String playtime) {
            this.name = name;
            this.start = convertTime(start);
            this.playtime = Integer.parseInt(playtime);
        }
        
        public int convertTime(String time) {
            String[] times = time.split(":");
            
            String hour = times[0];
            String minute = times[1];
            
            return Integer.parseInt(hour) * 60 + Integer.parseInt(minute);
        }
    }
    
    class PlanComparator implements Comparator<Plan> {
        @Override
        public int compare(Plan o1, Plan o2) {
            return o1.start - o2.start;
        }
    }
    
    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        Plan[] stack = new Plan[plans.length];
        Plan[] newPlans = new Plan[plans.length];
        
        for (int i = 0; i < plans.length; i++) {
            Plan plan = new Plan(plans[i][0], plans[i][1], plans[i][2]);
            newPlans[i] = plan;
        }
        
        Arrays.sort(newPlans, new PlanComparator());
        
        int stackSize = 0;
        int answerSize = 0;
        
        for (int i = 0; i < newPlans.length - 1; i++) {
            System.out.println(newPlans[i].name + " " + newPlans[i].start + " " + newPlans[i].playtime);
            int restTime = newPlans[i + 1].start - newPlans[i].start;
            
            if (restTime >= newPlans[i].playtime) {
                answer[answerSize++] = newPlans[i].name;
                restTime -= newPlans[i].playtime;
                
                while (stackSize > 0 && restTime > 0) {
                    Plan temp = stack[stackSize - 1];
                    temp.playtime -= restTime;
                    
                    if (temp.playtime > 0) {
                        restTime = 0;
                    } else {
                        stack[stackSize - 1] = null;
                        stackSize--;
                        restTime = -temp.playtime;
                        answer[answerSize++] = temp.name;
                    }
                }
            } else {
                newPlans[i].playtime -= restTime;
                stack[stackSize++] = newPlans[i];
            } 
        }
        
        answer[answerSize++] = newPlans[plans.length - 1].name;
        
        while (stackSize != 0) {
            answer[answerSize++] = stack[stackSize - 1].name;
            stackSize--;
        }
        
        return answer;
    }
}