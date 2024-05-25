#include <iostream>
#include <vector>

int64_t Sum(int64_t ind, const std::vector<int64_t> &sum) {
  int64_t local = 0;
  for (; ind >= 0; ind = (ind & (ind + 1)) - 1) {
    local += sum[ind];
  }
  return local;
}

void Addition(int64_t ind, int64_t delta, std::vector<int64_t> &sum) {
  for (; ind < (int64_t)sum.size(); ind = ind | (ind + 1)) {
    sum[ind] += delta;
  }
}

int main() {
  int64_t num;
  std::cin >> num;
  int64_t left;
  int64_t right;
  std::vector<int64_t> sum(num, 0);
  for (int64_t i = 0; i < num; i++) {
    int64_t tmp;
    std::cin >> tmp;
    Addition(i, tmp, sum);
  }
  int64_t pos;
  char operation;
  int64_t value;
  int64_t nQueries;
  std::cin >> nQueries;
  for (int64_t k = 0; k < nQueries; ++k) {
    std::cin >> operation;
    if (operation == 'u') {
      std::cin >> pos >> value;
      int64_t old = Sum(pos--, sum) - Sum(pos-- - 1, sum);
      Addition(pos, value - old, sum);
    } else {
      std::cin >> left >> right;
      std::cout << Sum(right--, sum) - Sum(left-- - 1, sum) << '\n';
    }
  }
}
