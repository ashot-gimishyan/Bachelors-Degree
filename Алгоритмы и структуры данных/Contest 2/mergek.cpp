#include <cstring>
#include <iostream>
#include <vector>

struct Node {

  int d;
  int ind;
};

int Parent(int i) { return (i - 1) / 2; }

int LeftSon(int i) { return 2 * i + 1; }

int RightSon(int i) { return 2 * i + 2; }

void SiftDown(Node *&a, Node *&b, int size, int ind, bool is_min) {
  int left = LeftSon(ind);
  int right = RightSon(ind);
  int ind_max = ind;

  if (right < size && left < size && a[right].d == a[left].d &&
      (is_min ? a[right].d < a[ind].d : a[right].d > a[ind].d)) {
    ind_max = left;
  } else {
    if (left < size &&
        (is_min ? a[left].d < a[ind_max].d : a[left].d > a[ind_max].d)) {
      ind_max = left;
    }

    if (right < size &&
        (is_min ? a[right].d < a[ind_max].d : a[right].d > a[ind_max].d)) {
      ind_max = right;
    }
  }

  if (ind_max != ind) {
    std::swap(b[a[ind].ind].ind, b[a[ind_max].ind].ind);
    std::swap(a[ind], a[ind_max]);
    SiftDown(a, b, size, ind_max, is_min);
  }
}

void SiftUp(Node *&a, Node *&b, int ind, bool is_min) {
  int i = ind;
  while ((is_min ? a[Parent(i)].d > a[i].d : a[Parent(i)].d < a[i].d) &&
         i > 0) {
    std::swap(b[a[i].ind].ind, b[a[Parent(i)].ind].ind);
    std::swap(a[i], a[Parent(i)]);
    i = Parent(i);
  }
}

int GetMin(Node *&a_min, Node *&a_max) { return a_min[0].d; }

int GetMax(Node *&a_min, Node *&a_max) { return a_max[0].d; }

void Insert(Node *&a_min, Node *&a_max, int &size) {
  int v;
  std::cin >> v;
  Node elem;
  elem.d = v;
  elem.ind = size;
  a_min[size] = elem;
  a_max[size] = elem;

  ++size;
  int temp_size = size - 1;
  SiftUp(a_min, a_max, temp_size, true);
  temp_size = size - 1;
  SiftUp(a_max, a_min, temp_size, false);

  std::cout << "ok" << std::endl;
}

int Extract(Node *&a, Node *&b, int size, int ind_to_delete, bool is_min) {
  std::swap(b[a[ind_to_delete].ind].ind, b[a[size - 1].ind].ind);
  std::swap(a[ind_to_delete], a[size - 1]);
  int result = a[size - 1].d;
  --size;
  if (ind_to_delete < size) {
    SiftDown(a, b, size, ind_to_delete, is_min);
    SiftUp(a, b, ind_to_delete, is_min);
  }
  return result;
}

void Clear(Node *&a_min, Node *&a_max, int &size) {
  size = 0;
  std::cout << "ok" << std::endl;
}

void ExtractMaxPrint(Node *&a_min, Node *&a_max, int size) {
  std::cout << GetMax(a_min, a_max) << std::endl;
  Extract(a_max, a_min, size, 0, false);
  Extract(a_min, a_max, size, a_max[size - 1].ind, true);
  size--;
}

void ExtractMinPrint(Node *&a_min, Node *&a_max, int size) {
  std::cout << GetMin(a_min, a_max) << std::endl;
  Extract(a_min, a_max, size, 0, true);
  Extract(a_max, a_min, size, a_min[size - 1].ind, false);
  size--;
}

int main() {
  int m;
  std::cin >> m;
  Node *a_min = new Node[m];
  Node *a_max = new Node[m];
  int size = 0;
  const int kBuf = 15;
  char operation[kBuf];
  for (int i = 0; i < m; ++i) {
    std::cin >> operation;
    if (strcmp(operation, "insert") == 0) {
      Insert(a_min, a_max, size);
    }
    if (strcmp(operation, "extract_min") == 0) {
      ExtractMinPrint(a_min, a_max, size);
    }
    if (strcmp(operation, "get_min") == 0) {
      std::cout << GetMin(a_min, a_max) << std::endl;
    }
    if (strcmp(operation, "extract_max") == 0) {
      ExtractMaxPrint(a_min, a_max, size);
    }
    if (strcmp(operation, "get_max") == 0) {
      std::cout << GetMax(a_min, a_max) << std::endl;
    }
    if (strcmp(operation, "size") == 0) {
      std::cout << size << std::endl;
    }
  }
}
