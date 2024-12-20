#include<iostream>
#include<queue>
#include<stack>
using namespace std;

//Min heap with 1 based indexing

class BinaryHeap {
private:
	vector <int> heap;

	int left(int parent) {
		return parent * 2;
	}
	int right(int parent) {
		return parent * 2 + 1;
	}

	int parent(int child) {
		return child / 2;
	}

	void heapifyUp(int index) {
		if (index > 1) {
			int parent = index / 2;
			if (heap[parent] > heap[index])
				swap(heap[parent] , heap[index]);

			heapifyUp(parent);
		}
	}

	void heapifyDown(int index) {
		while (index < heap.size() - 1) {
			int left = index * 2;
			int right = index * 2 + 1;

			int swapIndex = index;

			if (left < heap.size() && heap[index] > heap[left])
				swapIndex = left;

			else if (right < heap.size() && heap[swapIndex] > heap[right])
				swapIndex = right;

			if (index != swapIndex)
			{
				swap(heap[index], heap[swapIndex]);
				index = swapIndex;
			}
			else
				return;


		}
	}

	void heapify(int n, int i) {
		int left = i * 2;
		int right = i * 2 + 1;

		int swapIndex = i;

		if (left < heap.size() && heap[i] > heap[left])
			swapIndex = left;

		if (right < heap.size() && heap[swapIndex] > heap[right])
			swapIndex = right;

		if (i != swapIndex)
		{
			swap(heap[swapIndex], heap[i]);
			heapify(n, swapIndex);
		}
		else return;
	}

public:
	BinaryHeap()
	{
		heap.push_back(-1);
	}

	BinaryHeap(vector<int> arr) {
		heap = arr;

		int i = (heap.size() - 1) / 2; // last non-leaf node

		for (i ; i >= 1; i--)
			heapify(heap.size() - 1, i);
	}




	void displayHeap() {
		vector <int>::iterator pos = heap.begin();
		cout << "Heap -->  ";
		for (auto i : heap)
			if (i != -1)
				cout << i << ' ';
		cout << endl;
	}


	void insert(int value) {
		heap.push_back(value);
		heapifyUp(heap.size() - 1);
	}

	void deleteMin() {
		heap[1] = heap[heap.size() - 1];
		heap.pop_back();
		heapifyDown(1);
	}


};



int main() {

	BinaryHeap h;
	h.insert(50);
	h.insert(55);
	h.insert(53);
	h.insert(52);
	h.insert(54);


	h.displayHeap();

	h.deleteMin();
	h.displayHeap();


	// vector<int> arr = { -1, 3, 1, 6, 5, 2, 4};
	// BinaryHeap h(arr);
	// h.displayHeap();

	return 0;
}