import java.util.*;

class Solution {
    class Data {
        public int start, end;
    }
    
    public int solution(int[][] targets) {
        int answer = 0;
        ArrayList<Data> datas = new ArrayList<>();
        
        for (int[] target: targets) {
            Data data = new Data();
            data.start = target[0];
            data.end = target[1];
            datas.add(data);
        }

        Collections.sort(datas, new Comparator<Data>() {
            @Override
            public int compare(Data data1, Data data2) {
                if (data1.end == data2.end) {
                    return data1.start - data2.start;
                }
                return data1.end - data2.end;
            }
        });
        
        ArrayList<Data> fires = new ArrayList<>();
        
        int prev_end = -1;
        
        for (Data data: datas) {
            if (data.start >= prev_end) {
                answer++;
                prev_end = data.end;
            }
            // System.out.print(data.start);
            // System.out.println(data.end);
        }
        
        return answer;
    }
}