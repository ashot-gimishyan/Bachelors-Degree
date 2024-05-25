#include <bits/stdc++.h>

struct Rect {
  int x;
  int y;
};

int main() {
  int n, k;
  std::cin >> n >> k;

  std::vector<Rect> rects(n);

  for (int i = 0; i < n; ++i) {
    std::cin >> rects[i].x >> rects[i].y;
  }

  std::sort(rects.begin(), rects.end(), [](const Rect &left, const Rect right) {
    return left.y > right.y;
  });

  std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
  long long maxS = 0;

  for (const Rect &r : rects) {
    pq.push(r.x);
    if (pq.size() > k)
      pq.pop();

    assert(pq.size() <= k);

    if (pq.size() == k) {
      maxS = std::max(maxS, 1LL * r.y * pq.top());
    }
  }

  std::cout << maxS << std::endl;
  return 0;
}
