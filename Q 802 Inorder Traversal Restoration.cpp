/*A complete binary tree is a binary tree where every node except the leaf node has two child nodes and the last level of the tree for an edge-height h has 2^h leaf-nodes.

Your task is simple, given the postorder traversal for a complete binary tree, print it's inorder traversal.

The elements in the binary tree are of type character i.e. each node stores one character value.

Input Format

Only one string input denoting the postorder traversal.

Constraints

1 <= input.length <= 1000

Output Format

output one string that denotes the inorder traversal of the binary tree

Sample Input 0

BCA
Sample Output 0

BAC*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void inorder(char ch[],int l,int h){
    if(h-l==2)printf("%c%c%c",ch[l],ch[h],ch[l+1]);
    else{
        int m=(l+h)/2;
        inorder(ch,l,m-1);
        printf("%c",ch[h]);
        inorder(ch,m,h-1);
    }
}
int main() {
    char ch[1005];
    scanf("%s",ch);
    int n=strlen(ch);
    inorder(ch,0,n-1);
    return 0;
}
