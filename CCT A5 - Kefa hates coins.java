import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner (System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int ar[] = new int[a];
        int ar1[] = new int[b];
        for(int i = 0; i<a; i++ )
            ar[i] = sc.nextInt();
        for(int i = 0; i<b; i++ )
            ar1[i] = sc.nextInt();
        Arrays.sort(ar);
        int v[] =new int [a];
        int cc=0;
        for(int i = 0; i<b; i++ )
        {
            int sum=0;
            int count=0;
            for(int j = cc; j<a; j++ )
            {
                if(v[j]==0)
                {
                sum+=ar[j];
                v[j]=1;
                count++;
                cc++;
                }
                
                if(sum>=ar1[i])
                    break;                
            }
            if(count!=0&&sum!=0)
                System.out.println(count+" "+sum);
            else
                System.out.println("-1 -1");
                
        }
        
        
    }
}
