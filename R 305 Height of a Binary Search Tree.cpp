/*You are given N values to be inserted into a binary search tree. Every value in the left subtree fo a node x must be less than or equal to x and every value in the right subtree of a node x must be greater than x.
You are to insert the N values into a binary search tree in the order that they are given. Print the resultant binary search tree's height.

Input Format

First line contains a number N. Next line contains N integers.

Constraints

1 <= N <= 1000

Output Format

Output one integer that is the height of the binary search tree.

Sample Input 0

10
2 8 5 1 10 5 9 9 3 5 
Sample Output 0

6*/

#include <bits/stdc++.h>
using namespace std;
class Node 
{
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d)
        {
            data = d;
            left = NULL;
            right = NULL;
        }
};
class Solution
{
    public:
        Node* insert(Node* root, int data) 
        {
            if(root == NULL)           
                return new Node(data);
            else 
            {
                Node* cur;
                if(data <= root->data) 
                {
                    cur = insert(root->left, data);
                    root->left = cur;
                } 
                else
                {
                    cur = insert(root->right, data);
                    root->right = cur;
                }
               return root;
           }
        }
     int height(Node* root)
     {
        int leftHeight=-1,rightHeight=-1;
        if(root->left)
            leftHeight=height(root->left);
        if(root->right)
            rightHeight=height(root->right);
        return max(leftHeight,rightHeight)+1;
    }

}; 
int main()
{
  
    Solution myTree;
    Node* root = NULL;
    int t;
    int data;
    cin >> t;
    while(t-- > 0)
    {
        std::cin >> data;
        root = myTree.insert(root, data);
    }
    int height = myTree.height(root);    
    cout << (height+1);
    return 0;
}
