#include <iostream>
#include <vector>

auto FenwickFunc(const int64_t &m) { return (m & (m + 1)); }

auto SequenceFunc(const int64_t &i_m) { return (i_m | (i_m + 1)); }

struct Coord {
  int64_t one;
  int64_t two;
  int64_t three;

  Coord() : one(0), two(0), three(0) {}

  Coord(int64_t x, int64_t y, int64_t z) : one(x), two(y), three(z) {}
};

// Binary Indexed Tree
class BIT {
  std::vector<std::vector<std::vector<long long>>> tree_;

public:
  BIT(int64_t size) {
    tree_.resize(size, std::vector<std::vector<long long>>(
                           size, std::vector<long long>(size, 0)));
    for (int64_t x = 0; x < size; ++x) {
      for (int64_t y = 0; y < size; ++y) {
        for (int64_t z = 0; z < size; ++z) {
          tree_[x][y][z] = 0;
        }
      }
    }
  }

  void Update(long long new_val, const Coord &coord) {
    const int64_t N = tree_.size();
    const int64_t x = coord.one, y = coord.two, z = coord.three;
    for (int64_t i = x; i < N; i = SequenceFunc(i)) {
      for (int64_t j = y; j < N; j = SequenceFunc(j)) {
        for (int64_t k = z; k < N; k = SequenceFunc(k)) {
          tree_[i][j][k] += new_val;
        }
      }
    }
  }

  auto Query(const Coord &coord) {
    long long res = 0;
    const int64_t x = coord.one, y = coord.two, z = coord.three;
    for (int64_t i = x; i >= 0; i = FenwickFunc(i) - 1) {
      for (int64_t j = y; j >= 0; j = FenwickFunc(j) - 1) {
        for (int64_t k = z; k >= 0; k = FenwickFunc(k) - 1) {
          res += tree_[i][j][k];
        }
      }
    }
    return res;
  }

  auto Query(const Coord &first, const Coord &second) {
    auto x1 = first.one, y1 = first.two, z1 = first.three, x2 = second.one,
         y2 = second.two, z2 = second.three;
    return Query(second) - Query(Coord(x1 - 1, y2, z2)) -
           Query(Coord(x2, y1 - 1, z2)) - Query(Coord(x2, y2, z1 - 1)) +
           Query(Coord(x1 - 1, y1 - 1, z2)) -
           Query(Coord(x1 - 1, y1 - 1, z1 - 1)) +
           Query(Coord(x1 - 1, y2, z1 - 1)) + Query(Coord(x2, y1 - 1, z1 - 1));
  }
};

int main() {
  int64_t req = 0;
  int64_t size;
  std::cin >> size;
  BIT tree(size);
  while (req != 3) {
    std::cin >> req;
    switch (req) {
    case 1:
      int64_t x;
      int64_t y;
      int64_t z;
      int64_t k;
      std::cin >> x >> y >> z >> k;
      tree.Update(k, Coord(x, y, z));
      break;
    case 2:
      int64_t x1;
      int64_t y1;
      int64_t z1;
      int64_t x2;
      int64_t y2;
      int64_t z2;
      std::cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
      std::cout << tree.Query(Coord(x1, y1, z1), Coord(x2, y2, z2)) << '\n';
      break;
    }
  }
}
