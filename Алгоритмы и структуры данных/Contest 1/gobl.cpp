#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>

int main()
{
    int n;
    std::cin >> n;
    std::deque<int> first, second;
    for (int z = 0; z < n; ++z) {
        char ch;
        std::cin >> ch;
        if (ch == '+') {
            int i;
            std::cin >> i;
            first.push_back(i);
            if (first.size() > second.size()) {
                second.push_back(first.front());
                first.pop_front();
            }
        }
        else if (ch == '*') {
            int i;
            std::cin >> i;
            first.push_front(i);
            if (first.size() > second.size()) {
                second.push_back(first.front());
                first.pop_front();
            }
        }
        else {
            std::cout << second.front() << "\n";
            second.pop_front();
            if (first.size() > second.size()) {
                second.push_back(first.front());
                first.pop_front();
            }
        }
    }
    return 0;
}
