import java.util.*;

class Solution {
    // L = -1 | R = +1
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    static int w;
    static int h;
    
    static int[][] map = new int[500][500];
    static int[][][] visited = new int[500][500][4];
    
    class Node {
        int x;
        int y;
        int dirt;
        
        Node(int x, int y, int dirt) {
            this.x = x;
            this.y = y;
            this.dirt = dirt;
        }
    }
    
    public int bfs(int sx, int sy, int dirt) {
        int cnt = 0;
        
        while (true) {
            dirt = (dirt + map[sx][sy] + 4) % 4;
            sx = (sx + dx[dirt] + h) % h;
            sy = (sy + dy[dirt] + w) % w;
            
            if (visited[sx][sy][dirt] == 1) {
                break;
            } else {
                cnt++;
                visited[sx][sy][dirt] = 1;
            }
        }
        
        return cnt;
    }
    
    public int[] solution(String[] grid) {
        int[] answer = {};
        
        h = grid.length;
        w = grid[0].length();
        
        for (int i = 0; i < grid.length; i++) {
            String temp = grid[i];
            
            for (int j = 0; j < temp.length(); j++) {
                if (temp.charAt(j) == 'L') {
                    map[i][j] = -1;
                } else if (temp.charAt(j) == 'R') {
                    map[i][j] = 1;
                } else {
                    map[i][j] = 0;
                }
            }
        }
        
        List<Integer> array = new ArrayList<>();
        
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                for (int k = 0; k < 4; k++) {
                    if (visited[i][j][k] == 0) {
                        int res = bfs(i, j, k);
                        visited[i][j][k] = 1;

                        if (res > 0) {
                            array.add(res);
                        }    
                    }
                }
            }
        }
        
        Collections.sort(array);
        
        answer = new int[array.size()];
        
        for (int i = 0; i < array.size(); i++) {
            answer[i] = array.get(i);
        }
        
        return answer;
    }
}