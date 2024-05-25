#include <iostream>
#include <vector>

int64_t fenwick_func(const int64_t &m) { return (m & (m + 1)); }

int64_t sequence_func(const int64_t &i_m) { return (i_m | (i_m + 1)); }

class BIT { // Binary Indexed Tree
  std::vector<std::vector<int64_t>> tree_;

public:
  BIT(int64_t num1, int64_t num2) {
    tree_.resize(num1, std::vector<int64_t>(num2, 0));
    for (int64_t i = 0; i < num1; ++i) {
      for (int64_t j = 0; j < num2; ++j) {
        tree_[i][j] = 0;
      }
    }
  }

  void Update(int64_t new_val, int64_t idx1, int64_t idx2) {
    const int64_t num1 = tree_.size();
    const int64_t num2 = tree_[0].size();
    for (int64_t i = idx1; i < num1; i = sequence_func(i)) {
      for (int64_t j = idx2; j < num2; j = sequence_func(j)) {
        tree_[i][j] += new_val;
      }
    }
  }

  int64_t Query(int64_t idx1, int64_t idx2) {
    int64_t res = 0;
    for (int64_t i = idx1; i >= 0; i = fenwick_func(i) - 1) {
      for (int64_t j = idx2; j >= 0; j = fenwick_func(j) - 1) {
        res += tree_[i][j];
      }
    }
    return res;
  }

  int64_t Query(int64_t x_1, int64_t y_1, int64_t x_2, int64_t y_2) {
    return Query(x_2, y_2) - Query(x_2, y_1 - 1) - Query(x_1 - 1, y_2) +
           Query(x_1 - 1, y_1 - 1);
  }
};

std::pair<int64_t, int64_t> MinMax(int64_t x, int64_t y) {
  return std::make_pair(std::min(x - 1, y - 1), std::max(x - 1, y - 1));
}

int main() {
  int num1;
  int num2;
  std::cin >> num1 >> num2;
  int requests;
  std::cin >> requests;
  BIT tree(num1, num2);
  for (int i = 0; i < requests; ++i) {
    int tmp;
    std::cin >> tmp;
    int64_t x_1, y_1, value;
    switch (tmp) {
    case 1:
      std::cin >> x_1 >> y_1 >> value;
      tree.Update(value, x_1 - 1, y_1 - 1);
      break;
    case 2:
      int64_t x_2, y_2;
      std::cin >> x_1 >> y_1 >> x_2 >> y_2;
      auto [a, c] = MinMax(x_1, x_2);
      auto [b, d] = MinMax(y_1, y_2);
      std::cout << tree.Query(a, b, c, d) << '\n';
      break;
    }
  }
}
