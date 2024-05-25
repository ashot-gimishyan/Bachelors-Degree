#include <cmath>
#include <iostream>
#include <string>
#include <vector>

long long Parent(long long index) { return (index - 1) / 2; }

long long LChild(long long index) { return (index + 1) * 2 - 1; }

long long RChild(long long index) { return (index + 1) * 2; }

class Node {
 public:
  int num_open;
  long long max_len;
  int num_close;
  Node() : num_open(0), max_len(0), num_close(0) {}

  Node(int open, int close, long long length)
      : num_open(open), max_len(length), num_close(close) {}
};

Node Merge(const Node& left, const Node& right) {
  const int kSize = std::min(left.num_open, right.num_close);
  int open = left.num_open + right.num_open - kSize;
  int close = left.num_close + right.num_close - kSize;
  long long length = left.max_len + right.max_len + kSize * 2;
  return Node{open, close, length};
}

class SegmentTree {
 public:
  SegmentTree(const std::string& speech) {
    long long k = std::log2(speech.size()) + 1;
    int kdegree_2 = (1 << (k));
    size_ = kdegree_2;
    long long size = 2 * size_ - 1;
    tree_.resize(size, Node());
    for (long long i = 0; i < static_cast<int>(speech.size()); ++i) {
      if (speech[i] == ')') {
        tree_[size_ + i - 1] = Node(0, 1, 0);
      }
      if (speech[i] == '(') {
        tree_[size_ + i - 1] = Node(1, 0, 0);
      }
    }
    for (long long i = size_ - 2; i >= 0; --i) {
      tree_[i] = Merge(tree_[LChild(i)], tree_[RChild(i)]);
    }
  }

  Node RMQ(long long left, long long right) {
    Node lb;
    Node rb;
    left += size_ - 1;
    right += size_ - 1;
    while (left < right) {
      auto r_brother = RChild(Parent(left));
      auto l_brother = LChild(Parent(right));
      if (left == r_brother) {
        lb = Merge(lb, tree_[left]);
      }
      if (right == l_brother) {
        rb = Merge(tree_[right], rb);
      }
      left = Parent(left + 1);
      right = Parent(right - 1);
    }
    if (left == right) {
      rb = Merge(tree_[left], rb);
    }
    return Merge(lb, rb);
  }

 private:
   std::vector<Node> tree_;
   long long size_;
};

int main() {
  std::string speech;
  std::cin >> speech;
  SegmentTree segment_tree(speech);

  int requests;
  std::cin >> requests;
  for (int i = 0; i < requests; ++i) {
    long long left;
    long long right;
    std::cin >> left >> right;
    auto answer = segment_tree.RMQ(left - 1, right - 1).max_len;
    std::cout << answer << '\n';
  }
}
