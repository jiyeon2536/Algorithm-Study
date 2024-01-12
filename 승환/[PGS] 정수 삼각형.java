import java.util.Arrays;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int n = triangle.length;
        int m = triangle[n - 1].length;
        int[][] dp = new int[n][m];
        for(int i=0; i < n; i++){
            dp[n-1][i] = triangle[n-1][i];
        }
        // System.out.println(Arrays.deepToString(dp));
        for(int i=n - 2; i >= 0; i--){
            for(int j=0; j <= i; j++){
                dp[i][j] = Math.max(triangle[i][j] + dp[i + 1][j],
                                    triangle[i][j] + dp[i + 1][j + 1]);
            // System.out.println(i + " " + j + " " + (triangle[i][j] + dp[i + 1][j]) + " " + (triangle[i][j] + dp[i + 1][j + 1]));
            }
            // System.out.println(Arrays.deepToString(dp));
        }
        answer = dp[0][0];
        
        return answer;
    }
}
