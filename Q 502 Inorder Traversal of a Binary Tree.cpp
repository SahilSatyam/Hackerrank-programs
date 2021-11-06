/*You are given a binary tree in the form of an array.

Binary tree is represented as an array in the following format :

the value of a node is stored in a[node].
the value for the left child of the node is stored in a[node + node]
the value for the right child of the node is stored in a[node + node + 1]
for any node, if a[node] is 0 it means the node is null
Given the array representation of a binary tree, print its Inorder Traversal

Input Format

First line contains the size of the array N.
Next line contains N integers denoting the array a.

Constraints

1 <= N <= 10^6
a[node] = 0 for node == null otherwise 1 <= a[node] <= 1000

Output Format

Print N integers, the inorder traversal path for the given binary tree.

Sample Input 0

15
1 2 3 4 0 5 6 0 0 0 0 0 0 7 8
Sample Output 0

4 2 1 5 3 7 6 8*/

#include <bits/stdc++.h>
using namespace std;
 
/* A binary tree node has data,
pointer to left child and a
pointer to right child */
struct Node
{
    int data;
    Node* left, * right;
};
 
/* Helper function that allocates a
new node */
Node* newNode(int data)
{
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}
 
// Function to insert nodes in level order
Node* insertLevelOrder(int arr[], Node* root,
                       int i, int n)
{
    // Base case for recursion
    if (i < n)
    {
        Node* temp = newNode(arr[i]);
        root = temp;
 
        // insert left child
        root->left = insertLevelOrder(arr,
                   root->left, 2 * i + 1, n);
 
        // insert right child
        root->right = insertLevelOrder(arr,
                  root->right, 2 * i + 2, n);
    }
    return root;
}
 
// Function to print tree nodes in
// InOrder fashion
void inOrder(Node* root)
{
    if (root != NULL && root->data != 0)
    {
        inOrder(root->left);
        cout << root->data <<" ";
        inOrder(root->right);
    }
}
 
// Driver program to test above function
int main()
{
    int n;
    cin >> n;
    int arr [n];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    Node* root = insertLevelOrder(arr, root, 0, n);
    inOrder(root);
}

