import java.util.*;

class Solution {
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    static int result = 0;
    
    static int[][] island = new int[101][101];
    
    public void dfs(int x, int y, int width, int height) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < height && ny >= 0 && ny < width && island[nx][ny] > 0) {
                result += island[nx][ny];
                island[nx][ny] = 0;
                dfs(nx, ny, width, height);
            }
            
        }
    }
    
    public int[] solution(String[] maps) {
        int[] answer = {};
        
        int height = maps.length;
        int width = maps[0].length();
        
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (maps[i].charAt(j) == 'X') {
                    island[i][j] = 0;
                } else {
                    island[i][j] = Integer.parseInt(maps[i].charAt(j) + "");
                }
            }
        }

        int size = 0;
        int[] temp = new int[100001];
        
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (island[i][j] > 0) {
                    result = island[i][j];
                    island[i][j] = 0;
                    dfs(i, j, width, height);
                    temp[size++] = result;
                }
            }
        }
        
        answer = new int[size];
        
        for (int i = 0; i < size; i++) {
            answer[i] = temp[i];
        }
        
        Arrays.sort(answer);
                
        if (size == 0) {
            answer = new int[] {-1};
        }
        
        return answer;
    }
}