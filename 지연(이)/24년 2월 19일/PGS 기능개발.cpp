#include <string>
#include <vector>
#include<iostream>
#include<cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int N = progresses.size();
    
    vector<int> stack;
    for(int i=0;i<N;i++){
        int tmp = ((100 - progresses[i]) / speeds[i]);
        if ((100-progresses[i])%speeds[i]!=0){
            tmp++;
        }
        stack.push_back(tmp);
    }
    
    int cnt = 1;
    int mx = stack[0];
    for(int i=1;i<N;i++){
        if(mx<stack[i]){
            answer.push_back(cnt);
            cnt=1;
            mx = stack[i];
        }
        else{
            cnt++;
        }
    }
    answer.push_back(cnt);
    
    return answer;
}
