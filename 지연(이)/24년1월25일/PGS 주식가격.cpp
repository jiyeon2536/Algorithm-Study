#include<iostream>
#include<vector>
#include<utility>
using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer(prices.size());
	vector<pair<int, int>> stack;
	
	for (int i = 0; i < prices.size(); i++) {
		if (stack.empty() || stack.back().second < prices[i]) {
			stack.push_back(make_pair(i, prices[i]));
		}
		else {
			while (!stack.empty()) {
				if (stack.back().second<=prices[i]) {
					break;
				}
				answer[stack.back().first] = i-stack.back().first;
				stack.pop_back();
			}
			stack.push_back(make_pair(i, prices[i]));
		}
	}

	while (!stack.empty()) {
		answer[stack.back().first] = prices.size() - 1 - stack.back().first;
		stack.pop_back();
	}
	return answer;
}
