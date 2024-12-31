#include<iostream>
using namespace std;

// Node Struct for AVL
struct Node{

    // Initialization of data members.
    int data;
    Node* left;
    Node* right;
    int height;

    // Node Constructor
    Node(int x){
        data = x;               
        left = right = nullptr;         // Left & Right Child NULL initially
        height = 1;                     // Height kept 1 inititally
    }

};


// Getter Function for Height
int getHeight(Node* node){

    if(!node){
        return 0;                       // If node is NULL, return 0
    }

    return node->height;                // Else get the height data member
}

// Function to calculate Balance Factor
int bf(Node* node){

    if(!node){
        return 0;                       // If node is NULL, return 0
    }

    // Balance Factor = Left child height - Right child height
    return getHeight(node->left) - getHeight(node->right);
}

// Function for Right Rotation
Node* rightRotate(Node* x){

    Node* y = x->left;
    Node* z = y->right;

    y->right = x;
    x->left = z;

    // Update heights (Height = max(left_height, right_height) + 1)
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;

    // Return updated "root" for the sub tree
    return y;

}

// Function for Left Rotation
Node* leftRotate(Node* x){

    Node* y = x->right;
    Node* z = y->left;

    y->left = x;
    x->right = z;

    // Update heights (Height = max(left_height, right_height) + 1)
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = max(getHeight(y->left), getHeight(x->right)) + 1;

    // Return updated "root" for the sub tree
    return y;

}

// Function to insert Values in the AVL
Node* insert(Node* root, int val){

    // If root is NULL, return new node.
    if(!root){
        return new Node(val);
    }

    // Following BST property, if root value > val, move to left child.
    else if(root->data > val){
        root->left = insert(root->left, val);
    }

    // Following BST property, if root value < val, move to right child.
    else if(root->data < val){
        root->right = insert(root->right, val);
    }

    // If val == root value, return. Duplicates not allowed in BST.
    else{
        return root;
    }

    // Update root height on insertion
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));

    // Check if node balanced after insertion.
    int bal_fac = bf(root);


   // Left Left Imbalance
    if (bal_fac > 1 && val < root->left->data) {
        return rightRotate(root);
    }

    // Left Right Imbalance
    if (bal_fac > 1 && val > root->left->data) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    // Right Right Imbalance
    if (bal_fac < -1 && val > root->right->data) {
        return leftRotate(root);
    }

    // Right Left Imbalance
    if (bal_fac < -1 && val < root->right->data) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    
    }
    return root;

}

int main(){

}