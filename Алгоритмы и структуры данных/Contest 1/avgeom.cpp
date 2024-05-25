#include <cmath>
#include <iostream>

struct Arrayindex {
  int arr[2];
};

void AvgeomPrint(int q, const long double* arr_log);

int main() {
  int n;
  std::cin >> n;
  long double* arr = new long double[n];
  long double * arr_log = new long double[n];

  for (int i = 0; i < n; ++i) {
    std::cin >> arr[i];
    if (i == 0) {
      arr_log[0] = log(arr[0]);
    } else {
      arr_log[i] = arr_log[i - 1] + log(arr[i]);
  }
}

  int q;
  std::cin >> q;
  AvgeomPrint(q, arr_log);
  delete[] arr;
  delete[] arr_log;

}


void AvgeomPrint(int q, const long double* arr_log) {
  long double res;
  Arrayindex* ind = new Arrayindex[q];

  for (int i = 0; i < q; i++) {
    res = 0;
    double sum_log = 0;
    for (int j = 0; j < 2; j++) {
      std::cin >> ind[i].arr[j];
    }

//       res /= diff;
//       res = exp(res);


    int start_index = ind[i].arr[0];
    int stop_index = ind[i].arr[1];

    if ( start_index != 0)
    {
      sum_log = arr_log[stop_index] - arr_log[start_index - 1];
    }
    else
    {
      sum_log = arr_log[stop_index];
    }

    long double diff = stop_index - start_index + 1;
    res = exp(sum_log/diff);

    const int num = 6;
    std::cout << std::fixed;
    std::cout.precision(num);
    std::cout << res << std::endl;
  }


 delete[] ind;

}
