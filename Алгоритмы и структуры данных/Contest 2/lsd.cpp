#include <iostream>

using namespace std;
typedef unsigned long long int ULL;

void LSDSort(ULL *a, const int arraySize) {
  ULL bucket[10], maxVal = 0, digitPosition = 1;
  int i;

  for (i = 0; i < arraySize; i++) {
    if (a[i] > maxVal) {
      maxVal = a[i];
    }
  }

  ULL pass = 1;
  while (maxVal / digitPosition > 0) {
    ULL digitCount[10] = {0};
    for (i = 0; i < arraySize; i++) {
      digitCount[a[i] / digitPosition % 10]++;
    }

    for (i = 1; i < 10; i++) {
      digitCount[i] += digitCount[i - 1];
    }

    for (i = arraySize - 1; i >= 0; i--) {
      bucket[--digitCount[a[i] / digitPosition % 10]] = a[i];
    }

    for (i = 0; i < arraySize; i++) {
      a[i] = bucket[i];
    }

    digitPosition *= 10;
  }
}

int main() {
  int N;
  std::cin >> N;
  ULL *a = new ULL[N];

  for (int i = 0; i < N; ++i) {
    cin >> a[i];
  }

  LSDSort(a, N);

  for (int i = 0; i < N; i++) {
    cout << a[i] << endl;
  }
}
