/*Your task is to write a program to print the zigzag level-order traversal of a binary tree.
Here are a few examples :

  1
 / \
2   3
Traversal : 1 3 2
    1
   / \
  2   3
 / \   \
4   5   6
Traversal : 1 3 2 4 5 6
       1
      / \
     2   3
    / \   \
   4   5   6
  /   /   / \
 7    8  9   10
 Traversal : 1 3 2 4 5 6 10 9 8 7
Input
First line contains the number of nodes N.
Next N-1 lines contains information about one edge each.
Each line consists of three values : U V C which denotes that V is a child of U
If C is 'L' then V is a left child and if C is 'R' then V is a right child

Output
Print the zigzag level order traversal as explained

Sample Input 0

3
1 2 L
1 3 R
Sample Output 0

1 3 2*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int t[1000000][2],s1[100000],s2[10000],t1=-1,t2=-1;
int main() {
    int n;scanf("%d",&n);
    int x,y;char c;
    for(int i=0;i<n-1;i++){
        scanf("%d %d %c",&x,&y,&c);
        if(c=='L')t[x][0]=y;
        else t[x][1]=y;
    }
    s1[++t1]=1;
    while(t1!=-1||t2!=-1){
        while(t1!=-1){
            int x=s1[t1--];printf("%d ",x);
            if(t[x][0]!=0)s2[++t2]=t[x][0];
            if(t[x][1]!=0)s2[++t2]=t[x][1];
        }
        while(t2!=-1){
            int x=s2[t2--];printf("%d ",x);
            if(t[x][1]!=0)s1[++t1]=t[x][1];
            if(t[x][0]!=0)s1[++t1]=t[x][0];
        }
    }
    return 0;
}
