class Solution {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int size = 0;
        
        int[][] maps = new int[rows][columns];
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                maps[r][c] = r * columns + c + 1;
            }
        }
        
        for (int[] query: queries) {
            int x1 = query[0] - 1;
            int y1 = query[1] - 1;
            int x2 = query[2] - 1;
            int y2 = query[3] - 1;
            
            int res = rotate(maps, x1, y1, x2, y2);
            answer[size++] = res;
        }
        
        return answer;
    }
    
    public int rotate(int[][] maps, int x1, int y1, int x2, int y2) {
        int min_num = maps[x1][y1];
        int[][] temp = new int[maps.length][maps[0].length];
        
        for (int r = 0; r < maps.length; r++) {
            for (int c = 0; c < maps[0].length; c++) {
                temp[r][c] = maps[r][c];
            }
        }
        
        int x = x1;
        int y = y1;
        int dirt = 0;
        
        while (dirt < 4) {
            int nx = x + dx[dirt];
            int ny = y + dy[dirt];
            
            
            if (nx >= x1 && nx <= x2 && ny >= y1 && ny <= y2) {
                temp[nx][ny] = maps[x][y];
                
                if (min_num > temp[nx][ny]) min_num = temp[nx][ny];
                
                x = nx;
                y = ny;   
            } else {
                dirt++;
            }
        }
        
        for (int r = 0; r < maps.length; r++) {
            for (int c = 0; c < maps[0].length; c++) {
                maps[r][c] = temp[r][c];
            }
        }
        
        return min_num;
    }
}