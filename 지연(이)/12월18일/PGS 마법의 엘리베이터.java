class Solution {
    public int solution(int storey) {
        int answer = 0;
        int tmp = storey;

        while (storey>0){
            tmp = storey%10;
            if ((tmp<5) || (tmp==5 && storey<10) || (tmp==5 && (storey%100/10)<5)){
                answer += tmp;
            } else{
                storey+=(10-tmp);
                answer+=(10-tmp);
            }
            storey/=10;
        }
        return answer;
    }
}
