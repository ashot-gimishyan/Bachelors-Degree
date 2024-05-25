#include <iostream>

int main()
{
    int ch, a = 0, b = 0, c = 0;
    int i = 0;
    int * arr = new int[100000];

    do {
        ch = getchar();
        arr[i] = ch;

        if (ch == '(')
            a++;
        else if (ch == ')' && --a < 0)
            break;

        if (ch == '{')
            b++;
        else if (ch == '}' && --b < 0)
            break;

        if (ch == '[')
            c++;
        else if (ch == ']' && --c < 0)
            break;

        if (']' == arr[i] && '(' == arr[i - 1]) {
            std::cout << "NO" << std::endl;
            exit(0);
        }

        if ('}' == arr[i] && '(' == arr[i - 1]) {
            std::cout << "NO" << std::endl;
            exit(0);
        }

        if (')' == arr[i] && '[' == arr[i - 1]) {
            std::cout << "NO" << std::endl;
            exit(0);
        }

        if ('}' == arr[i] && '[' == arr[i - 1]) {
            std::cout << "NO" << std::endl;
            exit(0);
        }

        if (')' == arr[i] && '{' == arr[i - 1]) {
            std::cout << "NO" << std::endl;
            exit(0);
        }

        if (']' == arr[i] && '{' == arr[i - 1]) {
            std::cout << "NO" << std::endl;
            exit(0);
        }

        ++i;

    } while (ch != '\n');


    if (a!= 0 || b != 0 || c != 0) {
        std::cout << "NO" << std::endl;
        exit(0);
    }

    std::cout << "YES" << std::endl;
    delete[] arr;
    return 0;
}
