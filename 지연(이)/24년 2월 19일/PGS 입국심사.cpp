#include<bits/stdc++.h>
using namespace std;

// 숫자가 크면 이분탐색을 시도해볼 것.

long long solution(int n, vector<int> times) {
    long long answer = 1e10; // max

    long long start = 0;
    long long end = 0;
    long long mid;
    long long people = 0;
    for (auto time : times) {
        if (end < time) end = time;
    }
    end *= n;

    while (start <= end) {
        mid = (start + end) / 2;
        people = 0;
        for (int i = 0; i < times.size(); i++) {
            people += mid / times[i];
        }

        if ( people < n ) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
            answer = mid;
            // if (answer > mid) answer = mid;
        }
    }
    return answer;
}
