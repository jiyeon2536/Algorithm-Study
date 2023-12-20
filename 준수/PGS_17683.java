import java.lang.Math;

class Solution {
    class Music {
        int time;
        String name;
        String melody;
        
        Music(int time, String name, String melody) {
            this.time = time;
            this.name = name;
            this.melody = "";

            int idx = 0;
            int jdx = 0;
            
            while (idx <= time) {
                this.melody += melody.charAt(jdx++);
                
                if (jdx >= melody.length()) {
                    jdx = 0;
                }
                
                idx++;
            }
        }
        
        public boolean compareMelody(String m) {
            int i = 0;
            int end = this.melody.length() - m.length();
            
            while (i <= end) {
                if (m.equals(this.melody.substring(i, i + m.length()))) {
                    return true;
                };
                
                i++;
            }
            
            return false;
        }
    }
    
    public String mappingMelody(String str) {
        String res = "";
        int idx = 0;
        
        while (idx < str.length()) {
            String temp = "";
            temp += str.charAt(idx);
            idx++;
            
            if (idx < str.length() && str.charAt(idx) == '#') {
                temp = temp.toLowerCase();
                idx++;
            }
            
            res += temp;
        }
        
        return res;
    }
    
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        int size = 0;
        int max_time = -1;
        
        m = mappingMelody(m);
        
        for (String musicinfo: musicinfos) {
            String[] info = musicinfo.split(",");
            
            String[] time = new String[2];
            int startTime, endTime;
            
            time = info[0].split(":");
            startTime = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
            time = info[1].split(":");
            endTime = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
            
            info[3] = mappingMelody(info[3]);
            
            Music music = new Music(Math.abs(endTime - startTime), info[2], info[3]);
            boolean result = music.compareMelody(m);
            
            if (result && music.time > max_time) {
                answer = music.name;
                max_time = music.time;
            }
        }
        
        if (answer.equals("")) {
            return "(None)";
        }
        
        return answer;
    }
}