#include <iostream>
#include <cmath>

int main(int argc, char const* argv[])
{

    long long N, x;
    std::cin >> N;

    while (N > 0) {
        std::cin >> x;
        for (long long i = 2; i <= sqrt(x);) {
            while (x % i == 0) {
                std::cout << i << ' ';
                x /= i;
            }
            i++;
        }
        if (x != 1)
            std::cout << x << ' ';

        --N;
        std::cout << '\n';
    }
    return 0;
}
