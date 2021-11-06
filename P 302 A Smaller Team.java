/*A Smaller Team

The coach from the previous problem has now changed his mind. He only wants to take n-k people into the team. He asks the first person in the line to go find the shortest person and switch places with him. He then asks the second person in line to go find the second shortest person and switch places with him. So on, until the kth person has switched with the Kth shortest person in front of the line.

Formally, swap the first element of the array with the smallest element of the array, then second element of the array with the second smallest element in the array and so on. Repeat this process k times.

INPUT

The first line of input is n (1≤n≤100), the number of applicants for the basketball team The second line of input is the heights of the n players (distinct positive numbers) each separated by a space. The third line of input is the number k (1≤k≤n)

OUTPUT

Print the heights of the players in a line after the k switches are complete.

Sample Input 0

7
4 9 6 3 1 7 5
4
Sample Output 0

1 3 4 5 6 7 9 */

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int a= sc.nextInt();
        int ar[] = new int[a];
        int ar1[] = new int[a];
        int temp1 = 0; 
        for(int i=0;i<a;i++)
        {
            ar[i]=sc.nextInt();
            ar1[i]=ar[i];
        }
        int b= sc.nextInt();
        Arrays.sort(ar);
        for(int i=0;i<b;i++)
        {
            int temp = ar[i],ind = 0;
            for(int j=0;j<a;j++)
            {
                if(ar1[j]==temp)
                {
                    ind = j;
                }
            }
            temp1 = ar1[i];
            ar1[i] = ar1[ind];
            ar1[ind] = temp1;
        }
        for(int j=0;j<a;j++)
        {
            System.out.print(ar1[j]+" ");
        }
        
    }
}
