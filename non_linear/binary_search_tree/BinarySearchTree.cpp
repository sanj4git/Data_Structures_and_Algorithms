#include<bits/stdc++.h>
using namespace std;

typedef struct Node {
	int data;
	Node* left;
	Node* right;

	Node(int value) : data(value), left(nullptr), right(nullptr) {}

} Node ;

class BST
{
private:
	Node* inserter(Node* root, int value) {
		if (root == nullptr)
			root = new Node(value);

		else {
			if (value < root->data)
				root->left = inserter( root->left, value);
			else
				root->right = inserter( root->right, value);
		}

		return root;
	}

public:
	Node*root;
	Node* lastSearchedNode = NULL;

	BST() : root(nullptr) {}


	void insert(int value) {
		root =	inserter(root, value);

	}

	void inorderTraversal(Node* root) {
		if (root != nullptr) {
			inorderTraversal(root->left);
			cout << root->data << " ";
			inorderTraversal(root->right);
		}
	}//anything is fine

	void inorder() {
		inorderTraversal(root);
		cout << endl;
	}

	void search( int key, Node* root) {
		if (root == NULL)
		{
			cout << "Not Found\n" << endl;
		}
		else {
			if (root->data == key) {
				cout << "Found" << endl;
				return;
			}
			else if (key < root->data)
				search( key, root->left);
			else if (key > root->data)
				search(key, root->right);
		}
	}

	int height(Node* root) {
		if (root == NULL)
			return -1;
		else {
			int leftHeight = height(root->left);
			int rightHeight = height(root->right);

			return max(leftHeight, rightHeight) + 1;
		}
	}

	bool isBalanced(Node* root) {
		if (root == NULL)
			return true;
		else {
			int leftHeight = height(root->left);
			int rightHeight = height(root->right);

			if (abs(leftHeight - rightHeight) <= 1 &&
			        isBalanced(root->left) && isBalanced(root->right))
				return true;

			else
				return false;

		}
	}

	void printLevel(Node* root, int level, int l2r) {
		if (root == NULL)
			return;
		else {
			if (level == 0)
				cout << root->data << " ";

			else if (l2r == 1 && level > 0) {
				printLevel(root->left, level - 1, l2r);
				printLevel(root->right, level - 1, l2r);
			}

			else if (l2r == 0 && level > 0) {
				printLevel(root->right, level - 1, l2r);
				printLevel(root->left, level - 1, l2r);
			}
		}

	}

	void printSpiralOrder() {
		int h = height(root);

		for (int i = 0; i <= h; i++)
		{
			printLevel(root, i, i % 2);
			cout << endl;
		}
	}

	void printLevelOrder() {
		int h = height(root);

		for (int i = 0; i <= h; i++)
		{
			printLevel(root, i, 1);
			cout << endl;
		}

	}

	Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {

		if (root == NULL || root == p  || root == q)
			return root;

		Node* left = lowestCommonAncestor(root->left, p, q);
		Node* right = lowestCommonAncestor(root->right, p, q);

		if (!left)
			return right;

		else if (!right)
			return left;

		else
			return root;

	}

	Node*  searchNode(Node* root, int key) {
		if (root == NULL)
			return NULL;

		else {
			if (root->data == key)
				return root;
			else if (key < root->data)
				searchNode(root->left, key );
			else if (key > root->data)
				searchNode(root->right, key);
		}
	}

	Node* kthLargest(Node* root, int &k) {
		if (root == NULL)
			return root;

		Node* right = kthLargest(root->right, k);
		if (right)
			return right;
		k--;

		if (k == 0) return root;

		return kthLargest(root->left, k);
	}

	Node* kthSmallest(Node* root, int &k) {
		if (root == NULL)
			return root;

		Node* left = kthSmallest(root->left, k);
		if (left)
			return left;
		k--;

		if (k == 0) return root;

		return kthSmallest(root->right, k);
	}

};

int main()
{
	BST t;

	t.insert(5);
	t.insert(3);
	t.insert(2);
	t.insert(4);
	t.insert(7);
	t.insert(6);
	t.insert(8);

	// t.level_order();
	// t.search( 14, t.root);

	// t.printLevelOrder();

	// t.printLevel(t.root, 2, 1);

	// Node* ans = t.lowestCommonAncestor(t.root, t.searchNode(t.root, 2), t.searchNode(t.root, 3));
	// cout << ans->data;


	int k = 3;
	int p = k;
	cout << t.kthLargest(t.root, k)->data << endl;
	k = p;

	p = k;
	cout << t.kthSmallest(t.root, k)->data << endl;
	k = p;


	return 0;
}