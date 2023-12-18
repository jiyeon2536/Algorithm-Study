import java.io.*;
import java.util.*;

class Solution {
    
    static int check;
    static int[] start = new int[2];
    static int[][] visited;
    static int[] di = {0, 1, 0, -1}, dj = {1, 0, -1, 0};
    
    
    public int[] solution(int m, int n, int[][] picture) {
        
        int[] answer = new int[2];
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        visited = new int[m][n];

      
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++){
                if (visited[i][j] == 0 && picture[i][j] != 0) {
                    start[0] = i;
                    start[1] = j;
                    check = bfs(m, n, picture, picture[i][j]);
                
                    numberOfArea += 1;
        
                    if (check > maxSizeOfOneArea) {
                        maxSizeOfOneArea = check;
                    }
                    
                }
            }
     
        }
   
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
        
        
    }
    
    public int bfs(int m, int n,int[][] picture, int num) {
        ArrayDeque<int[]> deq = new ArrayDeque();
        deq.add(start);
        visited[start[0]][start[1]] = 1;
        
        int wid = 1;
        
        while (!deq.isEmpty()) {
            int[] now = deq.pollFirst();
            for (int k = 0; k < 4; k++) {
                int ni = now[0] + di[k], nj = now[1] + dj[k];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && visited[ni][nj] == 0 && picture[ni][nj] == num) {
                    wid += 1;
                    int[] tmp = {ni, nj};
                    deq.add(tmp);
                    visited[ni][nj] = 1;
                }
            }
        }
        return wid;
        
    }
 
}
