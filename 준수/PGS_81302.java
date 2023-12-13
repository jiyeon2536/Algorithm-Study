class Solution {
    
    class coord {
        int x;
        int ox;
        int y;
        int oy;
        int cnt;
        
        coord(int ox, int oy, int x, int y, int cnt) {
            this.ox = ox;
            this.oy = oy;
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
    
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    public int[] solution(String[][] places) {
        int[] answer = {0, 0, 0, 0, 0};
        
        for (int i = 0; i < 5; i++) {
            coord[] queue = new coord[100000];
            int[][] maps = new int[5][5];
            
            int front = 0;
            int rear = 0;
            
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    char location = places[i][j].charAt(k);
                    
                    if (location == 'P') {
                        maps[j][k] = 1;
                        coord temp = new coord(j, k, j, k, 0);
                        queue[rear++] = temp;
                    } else if (location == 'O') {
                        maps[j][k] = 0;
                    } else {
                        maps[j][k] = -1;
                    }
                }
            }
            
            int nx, ny;
            int flag = 1;
            
            while (front < rear && flag == 1) {
                coord data = queue[front++];
                
                if (data.cnt > 1) continue;
                
                for (int j = 0; j < 4; j++) {
                    nx = data.x + dx[j];
                    ny = data.y + dy[j];
                    
                    if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5 || maps[nx][ny] == -1) continue;
                    
                    if (maps[nx][ny] == 1 && (data.ox != nx || data.oy != ny)) {
                        flag = 0;
                        
                        System.out.println(nx + " " + ny);
                        
                        break;
                    };
                    
                    if (maps[nx][ny] == 0) {
                        coord temp = new coord(data.ox, data.oy, nx, ny, data.cnt + 1);
                        queue[rear++] = temp;
                    }
                }
            }
            
            answer[i] = flag;
        }
        
        return answer;
    }
}