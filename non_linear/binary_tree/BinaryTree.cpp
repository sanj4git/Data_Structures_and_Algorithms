#include<iostream>
#include<queue>
#include<stack>

using namespace std;

#define MAX_SIZE 25000

typedef struct Node {
	int data;
	Node* left;
	Node* right;

	Node(int value) : data(value), left(nullptr), right(nullptr) {}
} Node;

class BinaryTree {

	Node* inserter(Node* root, int key) {
		Node* newnode = new Node(key);

		if (root == nullptr)
		{
			root = newnode;
			return root;
		}
		else {

			Node* q[MAX_SIZE];
			int f, r;
			f = r = -1;


			q[++r] = root;
			f = r = 0;

			while (f <= r) {
				Node* temp = q[f];
				f++;

				if (temp->left != NULL)
					q[++r] = temp->left;

				else {
					temp->left = newnode;
					return root;
				}

				if (temp->right != NULL)
					q[++r] = temp->right;
				else {
					temp->right = newnode;
					return root;
				}

			}


		}

	}

public:
	Node* root;
	BinaryTree() {
		root = nullptr;
	}

	void insert(int key) {

		root = inserter(root, key);

	}

	void inorderTraversal(Node* root) {
		if (root == NULL)
			return ;

		inorderTraversal(root->left);
		cout << root->data << " ";
		inorderTraversal(root->right);

	}

	void mirror(Node* node) {

		if (node->right)
			mirror(node->right);
		if (node->left)
			mirror(node->left);

		swap(node->left, node->right);

	}

	void leafProduct(Node* root, int &product) {
		if (root->left == NULL && root->right == NULL)
			product *= root->data;

		else {
			leafProduct(root->left, product);
			leafProduct(root->right, product);
		}
	}

	void leafSum(Node* root, int &summ) {
		if (root->left == NULL && root->right == NULL)
			summ += (root->data);

		else {
			leafSum(root->left, summ);
			leafSum(root->right, summ);
		}
	}
};

int main() {
	BinaryTree t;

	t.insert(1);
	t.insert(2);
	t.insert(3);


	int product = 1, summ = 0;
	t.leafProduct(t.root, product);
	cout << product;

	t.leafSum(t.root, summ);
	cout << summ;

	// t.inorderTraversal(t.root);

	return 0;
}