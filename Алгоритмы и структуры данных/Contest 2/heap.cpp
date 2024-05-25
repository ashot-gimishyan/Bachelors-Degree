#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

struct Node {
  int key;
  int index;
};

bool compare(Node a, Node b) { return a.key > b.key; }

int parent(unsigned int index) { return (index - 1) / 2; }

int leftChild(unsigned int index) { return 2 * index + 1; }

int rightChild(unsigned int index) { return 2 * index + 2; }

void SiftDown(Node *heap, unsigned int index, int size, int *track_of_index) {
  int left, right, swap_index;
  left = leftChild(index);
  right = rightChild(index);
  swap_index = index;
  if (left < size && compare(heap[swap_index], heap[left])) {
    swap_index = left;
  }
  if (right < size && compare(heap[swap_index], heap[right])) {
    swap_index = right;
  }
  if (swap_index != index) {
    swap(track_of_index[heap[swap_index].index],
         track_of_index[heap[index].index]);
    swap(heap[swap_index], heap[index]);
    SiftDown(heap, swap_index, size, track_of_index);
  }
}

void SiftUp(Node *heap, unsigned int index, int *track_of_index) {
  while (index > 0 && compare(heap[parent(index)], heap[index])) {
    swap(track_of_index[heap[index].index],
         track_of_index[heap[parent(index)].index]);
    swap(heap[index], heap[parent(index)]);
    index = parent(index);
  }
}

int insert(Node *heap, Node value, int &size, int *track_of_index) {
  heap[size] = value;
  track_of_index[heap[size].index] = size;
  ++size;
  SiftUp(heap, size - 1, track_of_index);
  return 0;
}

void remove(Node *heap, int index, int &size, int *track_of_index) {
  swap(track_of_index[heap[index].index], track_of_index[heap[size - 1].index]);
  swap(heap[size - 1], heap[index]);
  track_of_index[heap[size - 1].index] = -1;
  --size;
  SiftDown(heap, index, size, track_of_index);
  SiftUp(heap, index, track_of_index);
}

void clear(Node *heap, int &size, int *track_of_index) {
  for (int i = 0; i < size; i++) {
    track_of_index[heap[i].index] = -1;
  }
  size = 0;
}

int main() {
  int M, k, x, size = 0, element, insert_number = 0;

  cin >> M;

  char operation[20];

  int *track_of_index = new int[M + 1];
  for (int i = 0; i < M; ++i) {
    track_of_index[i] = -1;
  }
  Node *heap = new Node[M];

  Node temp;

  for (int i = 0; i < M; ++i) {
    cin >> operation;
    if (!strcmp(operation, "insert")) {
      cin >> element;
      temp.key = element;
      ++insert_number;
      temp.index = insert_number;
      insert(heap, temp, size, track_of_index);
      cout << "ok"
           << "\n";
    }
    if (!strcmp(operation, "extract_min")) {
      if (size > 0) {
        cout << heap[0].key << endl;
        remove(heap, 0, size, track_of_index);
      } else {
        cout << "error"
             << "\n";
      }
    }
    if (!strcmp(operation, "get_min")) {
      if (size > 0) {
        cout << heap[0].key << "\n";
      } else {
        cout << "error"
             << "\n";
      }
    }
    if (!strcmp(operation, "size")) {
      cout << size << endl;
    }
    if (!strcmp(operation, "clear")) {
      clear(heap, size, track_of_index);
      cout << "ok"
           << "\n";
    }
  }

  delete[] heap;
  delete[] track_of_index;

  return 0;
}
