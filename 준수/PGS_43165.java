class Solution {
    public static int answer = 0;
    
    void dfs(int idx, int[] numbers, int res, int target) {
        if (idx == numbers.length) {
            if (res == target) {
                answer++;
            }
            return;
        }
        
        dfs(idx + 1, numbers, res + numbers[idx], target);
        dfs(idx + 1, numbers, res - numbers[idx], target);
    }
    
    public int solution(int[] numbers, int target) {
        
        dfs(0, numbers, 0, target);
        
        return answer;
    }
}