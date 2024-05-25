#include <bits/stdc++.h>

int main() {
  int n;
  std::cin >> n;
  std::vector<int> v(n);

  for (int i = 0; i < n; ++i)
    std::cin >> v[i];

  sort(v.begin(), v.end(), std::greater<int>());

  int res = 0;
  while (v.size() != 1) {
    int a = v[n - 1];
    int b = v[n - 2];
    v.pop_back();
    v.pop_back();
    int sum = a + b;
    res += sum;
    v.push_back(sum);
    sort(v.begin(), v.end(), std::greater<int>());
    --n;
  }
  std::cout << std::setprecision(2) << std::fixed << res*0.05 << std::endl;
}
