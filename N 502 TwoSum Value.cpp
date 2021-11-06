/*For any given Array A[N], its TwoSum Value with respect to a number K is denoted by the number of ordered pairs {i, j} such that A[i] + A[j] = K.
i and j must satisfy the following :
1 <= i <= N and 1 <= j <= N.
i may be equal to j at times.
You are given the Array A[N] and the number K.
Find and print the TwoSum value for the array.

Hint : You may want to use binary search algorithm for efficient implementation.
Hint2 : BinarySearch works only on sorted Arrays. So you may want to use library sort (qsort in C and sort in C++) function to sort the array first.

INPUT

The first line contains a number N(1 <= N <= 10^5), the size of array A[N].
The second line contains N space separated integers denoting the elements of the array A. (1 <= A[i] <= 10^9).
The third line contains one number K(1 <= K <= 10^9), with respect to which the TwoSum value of the array A is to be found.

OUTPUT

Output one number that is equal to the TwoSum value of the given input array A[N] with respect to K.

Sample Input 0

10
1 2 3 4 5 6 7 8 9 10
10
Sample Output 0

9*/

#include <bits/stdc++.h>
using namespace std;
int bs(int x,int arr[],int n)
{
    int l=0;
    int h=n-1;
    
    while(l<=h)
    {  
     int mid=l+ (h-l)/2;
        int y=arr[mid];
     if(x==y)
     {
         return 1;
     }
     else if(x<y)
        {
            h=mid-1;
        }
     else
     {
         l=mid+1;
     }
         
    }
    return 0;
}
int main() {
int n;
   cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
    cin>>arr[i];
       
    }
    sort(arr,arr+n);
    int k;
    cin>>k;
    int f=0;
       for(int i=0;i<n;i++)
    {
  int z=  bs(k-arr[i],arr,n);
      if(z==1)
      {
          
          f++;
    } 
       }
    cout<<f;
   
    return 0;
}
