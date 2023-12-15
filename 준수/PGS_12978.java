import java.util.*;
import java.lang.Math;

class Solution {
    public class Node {
		int node;
		long dist;
		
		public Node(int node, long dist) {
			this.node = node;
			this.dist = dist;
		}
	}
    
    class NodeComparator implements Comparator<Node> {
        @Override
        public int compare(Node o1, Node o2) {
            if (o1.dist > o2.dist) {
                return 1;
            } else if (o1.dist < o2.dist) {
                return -1;
            } else {
                return 0;
            }
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        
        int[][] graph = new int[N + 1][N + 1];
        
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                graph[i][j] = 500001;
            }
        }

        for (int i = 0; i < road.length; i++) {
            graph[road[i][0]][road[i][1]] = Math.min(road[i][2], graph[road[i][0]][road[i][1]]);
            graph[road[i][1]][road[i][0]] = Math.min(road[i][2], graph[road[i][1]][road[i][0]]);
        }
        
        PriorityQueue<Node> pq = new PriorityQueue<>(1, new NodeComparator());

        long[] result = new long[N + 1];
        
        for (int i = 2; i < N + 1; i++) {
            result[i] = 500000000;
        }
        
        pq.add(new Node(1, 0));
        
        while (pq.peek() != null) {
            Node data = pq.remove();
            
            if (data.dist > result[data.node]) continue;
            
            for (int nxt = 1; nxt < N + 1; nxt++) {
                if (graph[data.node][nxt] > 0) {
                    if (result[nxt] > result[data.node] + graph[data.node][nxt]) {
                        result[nxt] = result[data.node] + graph[data.node][nxt];
                        pq.add(new Node(nxt, result[nxt]));
                    }
                }
            }
        }
        
        for (int nxt = 1; nxt < N + 1; nxt++) {
            if (result[nxt] <= K) answer++;
        }

        return answer;
    }
}