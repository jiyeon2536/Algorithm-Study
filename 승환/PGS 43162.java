import java.util.Arrays;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] chk = new boolean[n];
        for (int i=0; i < n; i++){
            if (!chk[i]){
                dfs(i, chk, computers);  // dfs돌려서 체크해준다.
                answer++;
            }
        }
        return answer;
    }
    public void dfs(int i, boolean[] chk, int[][] computers){
        chk[i] = true;
        for (int u=0; u < chk.length; u++){
            if(chk[u]){
                continue;
            }
            if (computers[i][u] == 1){
                dfs(u, chk, computers);
            }
        }
    }
}
