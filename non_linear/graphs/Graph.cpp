#include<bits/stdc++.h>
using namespace std;

class Graph {
	int numOfVertices;
	vector<int>* adjList;
	bool* visited;

public:

	Graph(int vertices) {
		numOfVertices = vertices;
		adjList = new vector<int>[numOfVertices];
	}

	void addEdge(int src, int dest) {
		adjList[src].push_back(dest);
		adjList[dest].push_back(src);
	}

	void BFS(int start) {
		visited = new bool[numOfVertices];
		for (int i = 0; i < numOfVertices; i++)
			visited[i] = false;

		queue<int> q;
		q.push(start);
		visited[start] = true;

		while (!q.empty()) {
			int front = q.front();
			cout << front << " ";
			q.pop();


			for (auto i : adjList[front] )
			{	if (!visited[i])
				{
					visited[i] = true;
					q.push(i);
				}
			}
		}
	}

	void DFS_iterative(int start) {
		vector<bool> visited(numOfVertices, false);

		stack<int> s;
		s.push(start);
		visited[start] = true;

		while (!s.empty()) {
			int top = s.top();
			s.pop();
			visited[top] = true;

			cout << top << endl;
			for (int i = adjList[top].size() - 1; i >= 0; i--) {
				int adjV = adjList[top][i];
				if (!visited[adjV]) {
					s.push(adjV);
					visited[adjV] = true;
				}
			}
		}

	}

};


int main() {

	Graph g(5);

	g.addEdge(0, 1);
	g.addEdge(0, 3);
	g.addEdge(0, 2);
	g.addEdge(1, 2);
	g.addEdge(2, 4);

	g.BFS(0); cout << endl;


	// Graph g(4);
	// g.addEdge(0, 1);
	// g.addEdge(0, 2);
	// g.addEdge(1, 2);
	// g.addEdge(2, 3);

	// g.DFS_iterative(0);

	return 0;
}