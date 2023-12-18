class Solution {
    static int O_cnt = 0;
    static int X_cnt = 0;
    static int O_done = 0;
    static int X_done = 0;
    
    static int[][] maps = new int[3][3];
    
    public void init(String[] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                char temp = board[i].charAt(j);
                
                if (temp == 'O') {
                    maps[i][j] = 1;
                    O_cnt++;
                } else if (temp == 'X') {
                    maps[i][j] = -1;
                    X_cnt++;
                }
            }
        }
    }
    
    public int check(int key) {
        if (maps[0][0] == key) {
            if (maps[0][0] == maps[0][1] && maps[0][1] == maps[0][2]) return 1;
            if (maps[0][0] == maps[1][0] && maps[1][0] == maps[2][0]) return 1;
        }
        
        if (maps[1][1] == key) {
            if (maps[1][1] == maps[1][0] && maps[1][1] == maps[1][2]) return 1;
            if (maps[1][1] == maps[0][1] && maps[1][1] == maps[2][1]) return 1;
            if (maps[1][1] == maps[0][0] && maps[1][1] == maps[2][2]) return 1;
            if (maps[1][1] == maps[0][2] && maps[1][1] == maps[2][0]) return 1;
        }
        
        if (maps[2][2] == key) {
            if (maps[2][2] == maps[2][1] && maps[2][1] == maps[2][0]) return 1;
            if (maps[2][2] == maps[1][2] && maps[1][2] == maps[0][2]) return 1;
        }
        
        return 0;
    }
    
    public int solution(String[] board) {
        int answer = 1;
        init(board);
        
        if (check(1) == 1) O_done = 1;
        if (check(-1) == 1) X_done = 1;
        
        if (O_cnt >= X_cnt) {
            if (O_cnt > X_cnt + 1) answer = 0;
            else if (O_done == 1 && X_done == 1) answer = 0;
            else if (O_done == 1 && O_cnt == X_cnt) answer = 0;
            else if (X_done == 1 && O_cnt > X_cnt) answer = 0;
            else answer = 1;
        } else answer = 0;
        
        return answer;
    }
}