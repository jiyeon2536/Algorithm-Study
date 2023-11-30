class Solution
{
    static int height;
    static int width;

    int[][] prefix = new int[1001][1001];
    
    public int solution(int [][]board)
    {
        int answer = board[0][0];
        
        height = board.length;
        width = board[0].length;

        for (int i = 1; i < height; i++) {
            for (int j = 1; j < width; j++) {
                if (board[i][j] == 1 && board[i - 1][j] == 1 && board[i][j - 1] == 1 && board[i - 1][j - 1] == 1) {
                    int min_value = 1001;
                    
                    if (min_value > prefix[i][j]) {
                        min_value = prefix[i][j];
                    }
                    
                    if (min_value > prefix[i][j + 1]) {
                        min_value = prefix[i][j + 1];
                    }
                    
                    if (min_value > prefix[i + 1][j]) {
                        min_value = prefix[i + 1][j];
                    }
                    
                    prefix[i + 1][j + 1] = min_value + 1;
                }
            }   
        }
        
        for (int i = 1; i < height + 1; i++) {
            for (int j = 1; j < width + 1; j++) {
                if (prefix[i][j] > 0 && prefix[i][j] + 1 > answer) answer = prefix[i][j] + 1;
            }
        }
        
        if (answer == 0 || answer == 1) {
            return answer;
        } else {
            return answer * answer;
        }
    }
}