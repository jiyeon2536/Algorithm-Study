class Solution {
    static int[] visited = new int[201];
    
    public void dfs(int[][] computers, int n, int node) {
                
        for (int i = 0; i < n; i++) {
            if (computers[node][i] == 1 && visited[i] == 0) {
                visited[i] = 1;
                dfs(computers, n, i);
            }   
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                dfs(computers, n, i);
                answer++;
            }
        }
        
        return answer;
    }
}