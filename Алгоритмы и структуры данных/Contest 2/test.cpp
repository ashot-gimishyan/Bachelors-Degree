#include <iostream>
#include <iomanip>
#include <set>

int main() {
  long res = 0;
  long quantity;
  std::cin >> quantity;

  std::multiset<int> nums;
  for (long i = 0; i < quantity; ++i) {
    long num;
    std::cin >> num;
    nums.insert(num);
  }

  while (nums.size() > 1) {
    auto first = nums.begin();
    auto second = next(first);
    auto third = next(second);
    long sum = *first + *second;
    nums.erase(first, third);
    res += sum;
    nums.insert(sum);
  }

  const float kPercent = 0.05;
  std::cout << std::setprecision(2) << std::fixed << res * kPercent
            << std::endl;
}
