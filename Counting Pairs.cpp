#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'countPairs' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY numbers
 *  2. INTEGER k
 */

int countPairs(vector<int> numbers, int k) {
    int n=numbers.size();
    int count = 0;
    sort(numbers.begin(), numbers.end());  // Sort array elements
    int l1=INT_MAX;
    int r1=INT_MAX;
    int l = 0;
    int r = 0;
    while(r < n)
    {
        if(l1==numbers[l])
        {
            l++;
        }
        if(r1==numbers[r])
        {
            r++;
        }
        else if(numbers[r] - numbers[l] == k)
        {
              count++;
              l1=numbers[l];
              r1=numbers[r];
              l++;
              r++;
        }
        else if(numbers[r] - numbers[l] > k)
        {
            l1=numbers[l];
            l++;
        }
            
        else
        {
            r1=numbers[r];
            r++;
            
        }
    }  
    return count;

}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string numbers_count_temp;
    getline(cin, numbers_count_temp);

    int numbers_count = stoi(ltrim(rtrim(numbers_count_temp)));

    vector<int> numbers(numbers_count);

    for (int i = 0; i < numbers_count; i++) {
        string numbers_item_temp;
        getline(cin, numbers_item_temp);

        int numbers_item = stoi(ltrim(rtrim(numbers_item_temp)));

        numbers[i] = numbers_item;
    }

    string k_temp;
    getline(cin, k_temp);

    int k = stoi(ltrim(rtrim(k_temp)));

    int result = countPairs(numbers, k);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
