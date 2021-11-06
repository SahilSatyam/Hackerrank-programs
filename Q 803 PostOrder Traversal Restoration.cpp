/*Given In-order and Pre-order traversals of a binary tree, you are to write the code that prints the post-porder traversal of the same binary tree.

Each node of the binary tree holds one character value.

The binary tree may or may not be complete.

Input Format

First line contains the inorder traversal.
Second line contains preorder traversal.

Constraints

Maximum number of nodes in the tree will be less than 100

Output Format

Output one string denoting the postorder traversal

Sample Input 0

DBEAFC
ABDECF
Sample Output 0

DEBFCA*/

#include<iostream>
#include<cstring>
using namespace std;
int search(char arr[], char x, int n){
    for (int i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}
void printPostOrder(char in[], char pre[], int n)
{
    char root = search(in, pre[0], n);
    if (root != 0)
        printPostOrder(in, pre + 1, root);
    if (root != n - 1)
        printPostOrder(in + root + 1, pre + root + 1, n - root - 1);
    cout << pre[0];
}
int main()
{
    char pre[100],in[100];
    cin>>in>>pre;
    int n=strlen(in);
    printPostOrder(in, pre, n);
    return 0;
}
