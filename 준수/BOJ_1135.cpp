#include <iostream>
#include <algorithm>
using namespace std;

#define MAX(x, y) ((x > y) ? (x) : (y))

void dfs(int N, int arr[], int answer[], int node) {
    int size = 0;
    int times[51];

    for (int i = 0; i < 51; i++)
    {
        times[i] = 0;
    }

    for (int i = 0; i < N; i++)
    {
        if (node == arr[i]) {
            dfs(N, arr, answer, i);
            times[size++] = answer[i];
        }
    }
    
    sort(times, times + size);

    for (int i = 0; i < size; i++)
    {
        times[i] -= i;
        if (times[i] < 0) times[i] = 0;
    }

    int max_time = 0;

    for (int i = 0; i < size; i++)
    {
        max_time = MAX(max_time, times[i]);
    }

    answer[node] = size + max_time;
}

int arr[51];
int answer[51];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    dfs(N, arr, answer, 0);

    cout << answer[0];

    return 0;
}
