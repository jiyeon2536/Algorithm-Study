class Solution {
    static int[][][] visited = new int[100][100][2];
    static int[][] queue = new int[20001][3];
    
    public int solution(String[] maps) {
        int answer = 0;
        
        int front = 0;
        int rear = 0;
        
        char temp;
        int ex = -1;
        int ey = -1;
        
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length(); j++) {
                temp = maps[i].charAt(j);
                
                if (temp == 'X') {
                    visited[i][j][0] = -1;
                    visited[i][j][1] = -1;
                } else if (temp == 'S') {
                    queue[rear][0] = i;
                    queue[rear][1] = j;
                    visited[i][j][0] = 1;
                    rear++;
                } else if (temp == 'E') {
                    ex = i;
                    ey = j;
                }
            }
        }
        
        int[] dx = new int[] { 1, 0, -1, 0 };
        int[] dy = new int[] { 0, 1, 0, -1 };
        
        int x, y, z, nx, ny;
        int height = maps.length;
        int width = maps[0].length();
        
        while (front != rear) {
            x = queue[front][0];
            y = queue[front][1];
            z = queue[front][2];
            front++;
            
            for (int i = 0; i < 4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];
                
                if ((nx >= 0 && nx < height) && (ny >= 0 && ny < width) && (visited[nx][ny][z] == 0)) {
                    temp = maps[nx].charAt(ny);
                    
                    if (temp == 'L') {
                        queue[rear][0] = nx;
                        queue[rear][1] = ny;
                        queue[rear][2] = 1;
                        visited[nx][ny][1] = visited[x][y][z] + 1;
                        rear++;
                    } else {
                        queue[rear][0] = nx;
                        queue[rear][1] = ny;
                        queue[rear][2] = z;
                        rear++;
                        visited[nx][ny][z] = visited[x][y][z] + 1;
                    }
                }
            }
        }
        
        answer = visited[ex][ey][1] - 1;
        
        return answer;
    }
}