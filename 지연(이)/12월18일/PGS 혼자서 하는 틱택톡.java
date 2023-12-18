import java.util.*;

class Solution{
    static int O = 0;
    static int X = 0;
    static int O_line = 0;
    static int X_line = 0;

    static int[][] maps = new int[3][3];

    public void init(String[] board){
        for(int i=0; i<3;i++){
            for(int j=0;j<3;j++){
                char temp = board[i].charAt(j);
                if (temp=='O'){
                    maps[i][j] = 1;
                    O++;
                }else if (temp=='X'){
                    maps[i][j]=-1;
                    X++;
                }
            }
        }
    }

    public int check(int key){
        for (int i=0;i<3;i++){
            if (key==maps[i][0] && maps[i][0]==maps[i][1] && maps[i][1]==maps[i][2]) return 1;
            if (key==maps[0][i] && maps[0][i]==maps[1][i] && maps[1][i]==maps[2][i]) return 1;
        }
        if (key==maps[0][0] && maps[0][0]==maps[1][1] && maps[1][1]==maps[2][2]) return 1;
        if (key==maps[2][0] && maps[2][0]==maps[1][1] && maps[1][1]==maps[0][2]) return 1;
        return 0;
    }

    public int solution(String[] board){
        int answer = 1;
        init(board);
        O_line = check(1);
        X_line = check(-1);

        if (O>=X){
            if (O>X+1) answer = 0;
            else if (O_line==1 && X_line==1) answer = 0;
            else if (O_line==1 && O==X) answer = 0;
            else if (X_line==1 && O>X) answer = 0;
            else answer = 1;
        }else answer = 0;

        return answer;
    }
}
