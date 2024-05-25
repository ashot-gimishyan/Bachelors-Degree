#include <iostream>
#include <vector>
#include <queue>

using namespace std;
typedef pair<int, pair<int, int> > ppi;

vector<int> MergeArrays(vector<vector<int> > arr) {
    vector<int> res;
    priority_queue<ppi, vector<ppi>, greater<ppi> > pq;
    for (int i = 0; i < arr.size(); i++)
        pq.push({ arr[i][0], { i, 0 } });
    while (pq.empty() == false) {
        ppi current = pq.top();
        pq.pop();
        int i = current.second.first;
        int j = current.second.second;
        res.push_back(current.first);
        if (j + 1 < arr[i].size())
            pq.push({ arr[i][j + 1], { i, j + 1 } });
    }
    return res;
}

int main()
{
    int k;
    cin >> k;
    vector<vector<int> > v;
    for (int i = 0; i < k; ++i) {
        int n;
        cin >> n;
        vector<int> temp;
        for (int j = 0; j < n; ++j) {
            int var;
            cin >> var;
            temp.push_back(var);
        }
        v.push_back(temp);
    }
    vector<int> res = MergeArrays(v);
    for (auto u : res) {
        cout << u << " ";
    }
    cout << endl;
}
