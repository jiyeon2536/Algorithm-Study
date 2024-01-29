#include<iostream>
#include<limits.h>

using namespace std;
int N, M;
int arr[501][501];
int visit[501][501];
int answer = INT_MIN;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};


void DFS(int x, int y, int Sum, int depth) {
	if (depth == 3) {
		answer = max(answer, Sum);
	}
	else {
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (nx>=0 && nx<N && ny>=0 && ny<M && visit[nx][ny]==0) {
				if (depth == 1) {
					visit[nx][ny] = 1;
					DFS(x, y, Sum + arr[nx][ny], depth + 1);
					visit[nx][ny] = 0;
				}
				visit[nx][ny] = 1;
				DFS(nx, ny, Sum + arr[nx][ny], depth + 1);
				visit[nx][ny] = 0;
			}
		}
	}
	
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
			visit[i][j] = 0;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visit[i][j] = 1;
			DFS(i, j, arr[i][j], 0);
			visit[i][j] = 0;
		}
	}
	cout << answer << "\n";
	return 0;
}
