#include <algorithm>
#include <iostream>

struct Node {
  Node *left;
  Node *right;
  long long lb, rb, sum, add;
};

long long temp = 0;

Node *Empty = new Node({nullptr, nullptr, 0, 0, 0, 0});

Node *build(int left, int right) {
  if (left + 1 == right) {
    return new Node({Empty, Empty, left, right, 0, 0});
  }
  int mid = (left + right) / 2;
  Node *nleft = build(left, mid);
  Node *nright = build(mid, right);
  return new Node({nleft, nright, left, right, 0, 0});
}

void change(Node *node, int ind, int add) {
  if (node->rb <= ind || node->lb > ind) {
    return;
  }
  if (node->lb + 1 == node->rb) {
    node->sum += add;
    return;
  }
  change(node->left, ind, add);
  change(node->right, ind, add);
  node->sum = node->left->sum + node->right->sum;
}

void push(Node *node) {
  if (node == Empty) {
    return;
  }
  node->sum += node->add * (node->rb - node->lb);
  node->left->add += node->add;
  node->right->add += node->add;
  node->add = 0;
}

void Print(Node *node, int ind) {
  push(node);
  if (node->rb <= ind || node->lb > ind) {
    return;
  }
  if (node->lb + 1 == node->rb) {
    temp = node->sum + node->add;
    return;
  }
  Print(node->left, ind);
  Print(node->right, ind);
  node->sum = node->left->sum + node->right->sum;
  return;
}

void changeOtr(Node *node, int left, int right, int add) {
  push(node);
  if (node->lb >= right || node->rb <= left) {
    return;
  }
  if (left <= node->lb && right >= node->rb) {
    node->add += add;
    push(node);
    return;
  }
  changeOtr(node->left, left, right, add);
  changeOtr(node->right, left, right, add);
  if (node == Empty) {
    return;
  }
  node->sum = node->left->sum + node->right->sum;
  return;
}

int main() {
  int num;
  std::cin >> num;
  long long arr[num];
  Node *tree_otr = nullptr;
  tree_otr = build(0, num);
  for (int i = 0; i < num; ++i) {
    std::cin >> arr[i];
    change(tree_otr, i, arr[i]);
  }
  int requests;
  char ch;
  int left;
  int right;
  int add;
  std::cin >> requests;
  for (int i = 0; i < requests; ++i) {
    std::cin >> ch;
    if (ch == 'g') {
      std::cin >> add;
      Print(tree_otr, add - 1);
      arr[add - 1] = temp;
      std::cout << arr[add - 1] << '\n';
    } else {
      std::cin >> left >> right >> add;
      changeOtr(tree_otr, left - 1, right, add);
    }
  }
}
