#include<limits.h>
#include <iostream>
#include <vector>
using namespace std;

#define V 6

int selectNextVertex(vector<bool> &visited, vector<int> &distance) {

	int nextVertex ;
	int minVal = INT_MAX;

	for (int i = 0; i < V; i++) {
		if (!visited[i] && distance[i] < minVal) {
			nextVertex = i;
			minVal = distance[i];
		}
	}
	return nextVertex;
}

void prims(int adj[V][V]) {

	vector<int> parent(V, -1);
	vector<bool> visited(V, false);
	vector<int> distance(V, INT_MAX);

	parent[0] = -1;
	distance[0] = 0;


	for (int i = 0; i < V - 1; i++) {

		int u = selectNextVertex(visited, distance);
		visited[u] = true;

		for (int j = 0; j < V; j++) {

			int adjWeight = adj[u][j];

			if ((adjWeight != 0 ) && !visited[j] && (distance[j] > adjWeight)) {
				distance[j] = adjWeight;
				parent[j] = u;
			}
		}

	}

	int sum = 0;
	for (int i = 1; i < V; i++) {
		cout << parent[i] << "~>" << i << endl;

		sum += adj[parent[i]][i];
	}
	cout << "TOTAL: " << sum << endl;

}

int main() {






	return 0;
}
