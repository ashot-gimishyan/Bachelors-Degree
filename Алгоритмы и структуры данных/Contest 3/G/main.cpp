#include <algorithm>
#include <iostream>

const int64_t kSup = 2000000000;
const uint64_t kConst = 16U;

struct Item {
  int64_t cnt;
  int64_t priority;
  int64_t x;
  int64_t min;
  Item* left;
  Item* right;
  Item() {}
  Item(int64_t x)
      : priority((rand() << kConst) + unsigned(rand())),
        x(x),
        min(x),
        left(nullptr),
        right(nullptr) {}
};

typedef struct Item* Pitem;
int64_t Min(int64_t lhs, int64_t rhs) { return (lhs < rhs) ? lhs : rhs; }
int64_t Cnt(Pitem item) { return item != nullptr ? item->cnt : 0; }
long long GetMin(Pitem item) { return item != nullptr ? item->min : kSup; }

void Upd(Pitem item) {
  if (item != nullptr) {
    item->cnt = 1 + Cnt(item->left) + Cnt(item->right);
    item->min = Min(item->x, Min(GetMin(item->left), GetMin(item->right)));
  }
}

void Merge(Pitem left, Pitem right, Pitem& node) {
  if (left == nullptr || right == nullptr) {
    node = left != nullptr ? left : right;
  } else if (left->priority > right->priority) {
    Merge(left->right, right, left->right), node = left;
  } else {
    Merge(left, right->left, right->left), node = right;
  }
  Upd(node);
}

void Split(Pitem node, Pitem& left, Pitem& right, int64_t pos) {
  if (node == nullptr) {
    return void(left = right = 0);
  }
  if (pos <= Cnt(node->left)) {
    Split(node->left, left, node->left, pos), right = node;
  } else {
    Split(node->right, node->right, right, pos - 1 - Cnt(node->left)),
        left = node;
  }
  Upd(node);
}

int main() {
  int64_t num;
  int64_t num1;
  int64_t num2;
  Pitem item;
  Pitem item1;
  Pitem item2;
  char symbol;
  std::cin >> num;
  for (int k = 0; k < num; ++k) {
    std::cin >> symbol >> num1 >> num2;
    if (symbol == '+') {
      Split(item, item1, item2, num1);
      Merge(item1, new Item(num2), item1);
      Merge(item1, item2, item);
    } else {
      Split(item, item, item1, num1 - 1);
      Split(item1, item1, item2, num2 - num1 + 1);
      std::cout << item1->min << std::endl;
      Merge(item, item1, item);
      Merge(item, item2, item);
    }
  }
}
