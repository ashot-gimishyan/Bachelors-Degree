#include <iostream>

const int num = 3;

struct BinSearch {
  int arr[num];
};

bool BinarySearch(int* begin, const int* end, int target);

int main() {
  int n;
  std::cin >> n;
  int* array = new int[n];
  for (int x = 0; x < n; ++x) {
    std::cin >> *(array + x);
  }

  int q;
  bool flag;
  std::cin >> q;
  BinSearch* bs = new BinSearch[q];

  for (int i = 0; i < q; i++) {
    for (int j = 0; j < num; j++) {
      std::cin >> bs[i].arr[j];
    }

    flag =
        BinarySearch(&array[bs[i].arr[0]], &array[bs[i].arr[1]], bs[i].arr[2]);

    if (flag) {
      std::cout << "YES\n";
    } else {
      std::cout << "NO\n";
    }
  }

  delete[] array;
  delete[] bs;
  return 0;
}

bool BinarySearch(int* begin, const int* end, int target) {
  while (end > begin) {
    int* middle = begin + (end - begin) / 2;

    if (*middle == target) {
      return true;
    }

    if (*middle > target) {
      end = middle;  // Value in [start, middle)
    } else {
      begin = middle + 1;  // Value in (middle, end)
    }
  }

  return false;
}
