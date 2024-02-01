#include<bits/stdc++.h>
#include<algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;

    int N = people.size();
    sort(people.begin(), people.end());

    int start = 0;
    int end = N - 1;

    while (start <= end) {
        if (people[start] + people[end] <= limit) {
            start += 1;
            end -= 1;
        }
        else {
            end -= 1;
        }
        answer += 1;
    }

    return answer;
}

int main() {
    vector<int> people = { 70, 50, 80 };
    int limit = 100;

    int answer = solution(people, limit);
    cout << answer << "\n";

    return 0;
}
