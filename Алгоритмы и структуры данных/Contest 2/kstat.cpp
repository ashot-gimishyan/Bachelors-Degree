#include <iostream>

int median(int* a, int p, int r)
{
  int res;
    int mid = (p + r) / 2;

    if (a[p] > a[r])
        if (a[r] > a[mid])
            res= r;
        else
            res= mid;
    else if (a[p] > a[mid])
        res= p;
    else
        res= mid;
  return res;
}

int partition(int* array, int p, int r)
{
    std::swap(array[r], array[median(array, p, r)]);
    int j = p;
    for (int i = p; i < r; i++)
        if (array[i] < array[r]) {
            std::swap(array[i], array[j]);
            j++;
        }
    std::swap(array[j], array[r]);
    return j;
}

int kStat(int* array, int n, int k)
{
    int p = 0;
    int r = n - 1;
    int q = partition(array, p, r);
    while (q != k) {
        if (k < q)
            r = q - 1;
        else
            p = q + 1;
        q = partition(array, p, r);
    }
    return array[q];
}

int main()
{

    int n, k, a_0, a_1;
    std::cin >> n >> k >> a_0 >> a_1;

    int a[n];
    a[0] = a_0;
    a[1] = a_1;

    for (int i = 2; i < n; i++) {
        a[i] = (a[i - 1] * 123 + a[i - 2] * 45) % (10000000 + 4321);
    }

    std::cout << kStat(a, n, k - 1);
}
