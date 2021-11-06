/*
When a tree is reflected across an imaginary straight vertical line right or left of the entire tree, the resultant tree hence obtained is the mirror tree of the original tree.

Your task is to write a program to check if two given trees are mirrors of each other.

Input
First line consists of the number of nodes N.
Next N-1 lines each describes the first tree. Each line has two integers U and V and a letter 'R' or 'L', denoting that V is the left or the right child of U.
Next N-1 lines each describes the second tree. Each line has two integers U and V and a letter 'R' or 'L', denoting that V is the left or the right child of U.

Output
Print "yes" if the two trees are mirrors of each other and "no" otherwise

Sample Input 0

3
1 2 R
1 3 L
1 2 L
1 3 R
Sample Output 0

yes
Explanation 0

The first tree is

  1 

 / \ 

3   2
The second tree is

  1 

 / \ 

2   3
Clearly, both the trees are mirrors of each other.
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int t1[1000][2],t2[1000][2];
int main() {
    int n; scanf("%d",&n);
    int x,y; char c;
    for(int i=0;i<n-1;i++)
    {
        scanf("%d%d %c",&x,&y,&c);
        if(c=='L')t1[x][0]=y;
        else t1[x][1]=y;
    }
    for(int i=0;i<n-1;i++)
    {
        scanf("%d%d %c",&x,&y,&c);
        if(c=='L')t2[x][0]=y;
        else t2[x][1]=y;
    }
    int f=0;
    for(int i=1;i<=n;i++)
    {
        if(t1[i][0]!=t2[i][1] && t1[i][1]!=t2[i][0])
        {
            f=1;break;
        }
    }
    if(f==0)printf("yes");
    else printf("no");
    return 0;
}
