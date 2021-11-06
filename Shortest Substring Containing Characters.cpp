#include <bits/stdc++.h>
using namespace std;

const int MAX_CHARS = 256;

string findSubString(string str)
{
    int n = str.length();

    int dist_count = 0;
    unordered_map<int, int> hash_map;
    for (int i = 0; i < n; i++) {
        hash_map[str[i]]++;
    }

    dist_count = hash_map.size();
    int size = INT_MAX;
    string res;
    for (int i = 0; i < n; i++) {
        int count = 0;
        int visited[256] = { 0 };
        string sub_str = "";
        for (int j = i; j < n; j++) {
            if (visited[str[j]] == 0) {
                count++;
                visited[str[j]] = 1;
            }
            sub_str += str[j];
            if (count == dist_count)
                break;
        }
        if (sub_str.length() < size && count == dist_count)
        {
            res = sub_str;
            size=res.length();
        }
    }
    return res;
}

int main()
{
    string str;
    cin>>str;
    cout << findSubString(str).length();
    return 0;
}
