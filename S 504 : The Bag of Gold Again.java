import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
            int n=sc.nextInt();
            int weight=sc.nextInt();
            int w[]=new int[n];
            int c[]=new int[n];
            for(int x=0;x<n;x++)
            {
                w[x]=sc.nextInt();
                c[x]=sc.nextInt();
            }
            int dp[][]=new int[n+1][weight+1];
            for(int x=1;x<=weight;x++)
            {
                for(int y=1;y<=n;y++)
                {
                    dp[y][x]=dp[y-1][x];
                    if(w[y-1]<=x)
                    {
                        dp[y][x]=Math.max(dp[y][x],dp[y-1][x-w[y-1]]+c[y-1]);
                    }
                    else
                    {
                        
                    }
                }
            }
            System.out.println(dp[n][weight]);
        }
    }
}
