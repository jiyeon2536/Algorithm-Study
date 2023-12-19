import java.lang.Math;

class Solution {
    static int result = 0;
    
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    public void dfs(int[][] picture, int x, int y, int m, int n, int color) {
        for (int move = 0; move < 4; move++) {
            int nx = x + dx[move];
            int ny = y + dy[move];
            
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && picture[nx][ny] == color) {
                picture[nx][ny] = 0;
                result += 1;
                dfs(picture, nx, ny, m, n, color);
            }
        }
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] > 0) {
                    result = 0;
                    dfs(picture, i, j, m, n, picture[i][j]);
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, result);
                }
            }
            
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}