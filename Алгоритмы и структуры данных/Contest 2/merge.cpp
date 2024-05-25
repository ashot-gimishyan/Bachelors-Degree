#include <iostream>
#include <vector>

using namespace std;

vector<int> Merge2Arrays(vector<int> first, vector<int> second)
{
    vector<int> ret;
    int f_in = 0, s_in = 0;
    while (f_in + s_in < first.size() + second.size()) {
        if (f_in != first.size() && (s_in == second.size() || first[f_in] < second[s_in])) {
            ret.push_back(first[f_in]);
            f_in++;
        }
        else {
            ret.push_back(second[s_in]);
            s_in++;
        }
    }
    return ret;
}

vector<int> MergeArrays(vector<vector<int> > arr)
{
    vector<vector<int> > arr_s;
    while (arr.size() != 1) {
        arr_s.clear();
        for (int i = 0; i < arr.size(); i += 2) {
            if (i == arr.size() - 1)
                arr_s.push_back(arr[i]);
            else
                arr_s.push_back(Merge2Arrays(arr[i], arr[i + 1]));
        }
        arr = arr_s;
    }
    return arr[0];
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

    vector<int> output = MergeArrays(v);
    for (auto u : output) {
        cout << u << " ";
    }
    cout << endl;
}
