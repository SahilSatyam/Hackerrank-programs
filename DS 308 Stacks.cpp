#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;
int main() {
    int n, k;
    stack<int> stk;
    
    cin>>n>>k;
    for(int i=0; i<k; i++){
        int temp;
        cin>>temp;
        stk.push(temp);
    }
    int p;
    cin>>p;
    
    for(int i=0; i<p; i++) stk.pop();
    
    while(!stk.empty()){
        cout<<stk.top()<<' ';
        stk.pop();
    }
    
    return 0;
}
