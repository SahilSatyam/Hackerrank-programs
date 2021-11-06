/*
Write a program to create a queue of size N specified by the user. Then you will be given a K value representing the number of elements to be inserted into the queue. After giving K no. of elements you will be given a P value. Then you have to delete the P no. of elements in the queue. After completion of entire process print the element from current starting position to ending position.

Input Format
First Line contains N value, the size of the queue
Second line contains K value followed by K no. of elements
Third line contains P value

Output Format
Print the elements from the current starting position to ending position.
Sample Input
5 4 1 2 3 4 2
Sample Output
3 4

Explanation We have to define the queue of size "5" and we have to insert "4" elements into it. 1 will be inserted into the queue first. Then on top of "1", "2" will be inserted and on top of "2", "3" will be inserted. Similarly "4".
After that you have to delete 2 elements from the queue, i.e., 1 and 2 will be deleted.
Now print the remaining elements

Sample Input:
5
4
1
2
3
4
2
Sample Output:
3 4
*/


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int main() {
    queue<int>q;
    int n;
    cin>>n;
    int k;
    cin>>k;
    int x;
    while(k--)
    {
        cin>>x;
        q.push(x);
    }
    int p;
    cin>>p;
    while(p--)
        q.pop();
    
    while(!q.empty())
    {
        cout<<q.front()<<" ";
        q.pop();
    }
    return 0;
}

