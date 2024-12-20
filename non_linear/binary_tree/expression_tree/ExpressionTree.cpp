#include<iostream>
#include<queue>
#include<stack>
using namespace std;

typedef struct node {
	char data;
	struct node*left, *right;

	node(char val) : data(val), right(nullptr), left(nullptr) {}
} node;

node* build(string& s)
{
	int priority[128] = {0};
	priority['+'] = priority['-'] = 1;
	priority['*'] = priority['/'] = 2;
	priority['^'] = 3;
	priority[')'] = 0;

	stack <char> charStack; //for storing symbols and brackets
	stack<node*> nodeStack; //for storing node pointers

	node* t, * t1, *t2; // t->parent, t1,t2->children

	for (int i = 0; i < s.size(); i++) { //iterate through infixstring

		if (s[i] == '(')
			charStack.push(s[i]);

		else if (isalpha(s[i]))
		{
			t = new node(s[i]);
			nodeStack.push(t);

		}

		else if (priority[s[i]] > 0) {

			while (
			    (!charStack.empty() && charStack.top() != '(')
			    &&
			    (
			        (s[i] != '^' && priority[charStack.top()] >= priority[s[i]])
// ||
// (s[i] == '^' && priority[charStack.top()] > priority[s[i]] )// to evaluate from right
			    )

			) {
				t = new node(charStack.top());
				charStack.pop();

				t1 = nodeStack.top(); nodeStack.pop(); //operand 2
				t2 = nodeStack.top(); nodeStack.pop(); //operand 1

				t->left = t2;  //     op     |    t
				t->right = t1; // op1   op2  | t2    t1

				nodeStack.push(t);
			}

			charStack.push(s[i]);
		}
		else if (s[i] == ')')
		{
			while (!charStack.empty() && charStack.top() != '(') {
				t = new node(charStack.top());
				charStack.pop();

				t1 = nodeStack.top(); nodeStack.pop();
				t2 = nodeStack.top(); nodeStack.pop();

				t->left = t2;
				t->right = t1;

				nodeStack.push(t);
			}
			charStack.pop();// popping the '('
		}
	}

	t = nodeStack.top(); //root node

	return t;
}

void postOrder(node* root) {
	if (root == NULL) return ;
	postOrder(root->left);
	postOrder(root->right);
	cout << root->data;
}

int main() {
	string s; cin >> s;

	s = "(" + s + ")";

	node*root = build(s);

	postOrder(root);
	return 0;
}