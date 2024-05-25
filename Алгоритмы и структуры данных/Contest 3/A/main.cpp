#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

class RMQ {
  std::vector<std::vector<int>> SP;

public:
  RMQ(const std::vector<int> &buff) {
    const int size = buff.size();
    int k = std::log2(size) + 1;
    SP.resize(k, std::vector<int>(size));
    for (int i = 0; i < k; ++i) {
      for (int j = 0; j < size; ++j) {
        if (i == 0) {
          SP[i][j] = buff[j];
        } else {
          int kdegree_2 = (1 << (i - 1));
          if ((j + kdegree_2) >= 0 && (j + kdegree_2) < size) {
            SP[i][j] = std::min(SP[i - 1][j], SP[i - 1][j + kdegree_2]);
          }
        }
      }
    }
  }

  int Query(int lb, int rb) {
    if (lb > rb) {
      std::swap(lb, rb);
    }
    int k = std::log2(rb - lb + 1);
    int kdegree_2 = 1 << k;
    return std::min(SP[k][lb], SP[k][rb - kdegree_2 + 1]);
  }
};

int main() {
  int num_soldiers, requests;
  std::cin >> num_soldiers >> requests;
  std::vector<int> length(num_soldiers);
  std::cin >> length[0];
  for (int i = 1; i < num_soldiers; ++i) {
    length[i] = (23 * length[i - 1] + 21563) % 16714589;
  }

  std::vector<int> lb(requests);
  std::vector<int> rb(requests);
  std::cin >> lb[0] >> rb[0];

  RMQ SP(length);
  for (int i = 1; i < requests; ++i) {
    int ans_i = SP.Query(lb[i - 1] - 1, rb[i - 1] - 1);
    lb[i] = (17 * lb[i - 1] + 751 + ans_i + 2 * (i)) % num_soldiers + 1;
    rb[i] = (13 * rb[i - 1] + 593 + ans_i + 5 * (i)) % num_soldiers + 1;
  }

  int ans = SP.Query(lb[requests - 1] - 1, rb[requests - 1] - 1);
  std::cout << lb[requests - 1] << " " << rb[requests - 1] << " " << ans;
}
