#include <iostream>

int main(int argc, char const* argv[])
{

    double x; // точка встречи на оси абсцисс
    int x_a, x_b, y_a, y_b;
    std::cin >> x_a >> y_a >> x_b >> y_b;

    if (x_a * x_b > 0)
        y_b = -y_b;

    if (y_a * y_b == 0)
        x = 0;
    else {
        // из уравнения прямой проходящей через две точки
        x = (((-y_a) / ((double)y_b - y_a)) * (x_b - x_a) + x_a);
    }

    std::cout << std::fixed;
    std::cout.precision(9);
    std::cout << x << '\n';

    return 0;
}
