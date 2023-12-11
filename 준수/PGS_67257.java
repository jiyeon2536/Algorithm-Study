import java.lang.Math;

class Solution {
    
    static long answer = -1;
    
    public static long cal2(String op, long a, long b) {
        if (op.equals("*")) return a * b;
        else if (op.equals("+")) return a + b;
        else return b - a;
    }
    
    public static void cal(String[] arr, int len, String f, String s, String t) {
        String[] stack = new String[100];
        String[] post = new String[100];
        int stack_size = 0;
        int post_size = 0;
        
        for (int i = 0; i < len; i++) {
            String elem = arr[i];
            
            if (elem.equals(f)) {
                if (post_size == 0) {
                    post[post_size++] = elem;
                    continue;
                }
                
                if (post[post_size - 1].equals(f)) {
                    stack[stack_size++] = post[post_size - 1];
                    post_size--;
                    post[post_size] = null;
                }
                
                post[post_size++] = elem;
            } else if (elem.equals(s)) {
                if (post_size == 0) {
                    post[post_size++] = elem;
                    continue;
                }
                
                while (post_size > 0 && (post[post_size - 1].equals(f))) {
                    stack[stack_size++] = post[post_size - 1];
                    post_size--;
                    post[post_size] = null;
                }
                
                if (post_size > 0 && post[post_size - 1].equals(s)) {
                    stack[stack_size++] = post[post_size - 1];
                    post_size--;
                    post[post_size] = null;
                }

                post[post_size++] = elem;
            } else if (elem.equals(t)) {
                if (post_size == 0) {
                    post[post_size++] = elem;
                    continue;
                }
                
                while (post_size > 0 && !post[post_size - 1].equals(t)) {
                    stack[stack_size++] = post[post_size - 1];
                    post_size--;
                    post[post_size] = null;
                }
                
                if (post_size > 0 && post[post_size - 1].equals(t)) {
                    stack[stack_size++] = post[post_size - 1];
                    post_size--;
                    post[post_size] = null;
                }

                post[post_size++] = elem;
            } else {
                stack[stack_size++] = elem;
            }
        }
        
        while (post_size > 0) {
            stack[stack_size++] = post[post_size - 1];
            post_size--;
            post[post_size] = null;
        }
        
        long[] num_stack = new long[100];
        int size = 0;
        int front = 0;
        long a, b;
        
        while (front < stack_size) {
            String elem = stack[front];
            
            if (elem.equals(f)) {
                size -= 1;
                a = num_stack[size--];
                b = num_stack[size];
                num_stack[size++] = cal2(f, a, b);
            } else if (elem.equals(s)) {
                size -= 1;
                a = num_stack[size--];
                b = num_stack[size];
                num_stack[size++] = cal2(s, a, b);
            } else if (elem.equals(t)) {
                size -= 1;
                a = num_stack[size--];
                b = num_stack[size];
                num_stack[size++] = cal2(t, a, b);
            } else {
                num_stack[size++] = Long.parseLong(elem);
            }
            
            front++;
        } 
        
        answer = Math.max(answer, Math.abs(num_stack[0]));
    }
    
    public long solution(String expression) {
        String[] arr = new String[100];
        int size = 0;
        String temp = "";
        String tc;
        
        for (int i = 0; i < expression.length(); i++) {
            tc = expression.charAt(i) + "";
            
            if (tc.equals("*") || tc.equals("+") || tc.equals("-")) {
                arr[size++] = temp;
                arr[size++] = tc;
                temp = "";
            } else {
                temp += tc;
            }
            
            if (i == expression.length() - 1) arr[size++] = temp;
        }
        
        cal(arr, size, "*", "+", "-");
        cal(arr, size, "*", "-", "+");
        cal(arr, size, "+", "*", "-");
        cal(arr, size, "+", "-", "*");
        cal(arr, size, "-", "*", "+");
        cal(arr, size, "-", "+", "*");
        
        return answer;
    }
}