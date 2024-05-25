#include <iostream>

long long nok(long long,long long);
long long nod(long long,long long);

int main(int argc, char const *argv[]) {
  long long a,b;
  std::cin >> a;
  std::cin >> b;
  std::cout << nok(a,b);
}

long long nod(long long a, long long b)
{
  if (a%b == 0)
    return b;
  if (b%a == 0)
    return a;
  if (a>b)
    return nod(a%b, b);
  else
    return nod(a, b%a);
}

long long nok(long long a, long long b)
{
  return a*b / nod(a, b);
}
