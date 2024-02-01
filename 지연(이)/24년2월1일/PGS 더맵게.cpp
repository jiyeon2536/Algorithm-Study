#include<bits/stdc++.h>
#include<queue>
#include <vector>

using namespace std;

int solution(vector<int> scoville, int k) {
    int answer = 0;

    priority_queue<int> pq;
    for (int i = 0; i < scoville.size(); i++) {
        pq.push(-scoville[i]);
    }

    while (pq.size()>1) {
        if (-pq.top() >= k) break;
        int n1 = -pq.top();
        pq.pop();
        int n2 = -pq.top();
        pq.pop();
        pq.push(-(n1 + n2 * 2));
        answer += 1;
    }
    if (pq.size() == 1 && -pq.top() < k) return -1;
    return answer;
}
