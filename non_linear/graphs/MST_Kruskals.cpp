#include<bits/stdc++.h>
using namespace std;
#define V 6

class DisjointSet {
	vector<int> size, parent;

public:
	DisjointSet(int v) {
		size.resize(v + 1, 1);
		parent.resize(v + 1, 0);

		for (int i = 0; i <= v; i++) {
			parent[i] = i;
		}
	}

	int findUltimatepar(int node) {
		if (node == parent[node]) return node;
		else
			return parent[node] = findUltimatepar(parent[node]);
	}

	void unionBySize(int u, int v) {
		int u_par = findUltimatepar(u);
		int v_par = findUltimatepar(v);

		if (u_par == v_par) return; // same parent so nothing to do

		else if (size[u_par] > size[v_par] ) {
			parent[v_par] = u_par;
			size[u_par] += size[v_par];
		}

		else {
			parent[u_par] = parent[v_par];
			size[v_par] += size[u_par];
		}

	}

};
void kruskals(int adj[V][V]) {

	DisjointSet checker(V);
	vector <pair<int, pair<int, int>>> edges;

	for (int i = 0 ; i < V ; i++) {
		for (int j = 0; j < V; j++) {
			if (adj[i][j] > 0) {
				edges.push_back({adj[i][j], {i, j}});

			}
		}
	}

	sort(edges.begin(), edges.end());

	int weightsum = 0;
	for (auto i : edges) {
		int src = i.second.first;
		int dest = i.second.second;
		int weight = i.first;

		if (checker.findUltimatepar(src) == checker.findUltimatepar(dest))
			continue;
		else {
			checker.unionBySize(src, dest);
			// checker.unionBySize(dest, src); not really needed as dsu ignores

			cout << src << "~>" << dest << endl;
			weightsum += weight;
		}
	}

	cout << weightsum << endl;

}

int main() {
	int graph[V][V] = {
		//0  1  2  3  4  5
		{0, 4, 6, 0, 0, 0},// 0
		{4, 0, 6, 3, 4, 0},// 1
		{6, 6, 0, 1, 8, 0},// 2
		{0, 3, 1, 0, 2, 3},// 3
		{0, 4, 8, 2, 0, 7},// 4
		{0, 0, 0, 3, 7, 0} // 5
	};

	kruskals(graph);



	return 0;
}