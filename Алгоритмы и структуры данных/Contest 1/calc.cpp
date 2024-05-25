#include <iostream>
#include <string>

struct Stack {
    int data;
    Stack* next;
};

void Push(Stack** top, int n)
{
    Stack* st = new Stack();
    st->data = n;
    if (*top == NULL) {
        *top = st;
    }
    else {
        st->next = *top;
        *top = st;
    }
}

int Pop(Stack** top)
{
    Stack* tmp = *top;
    if (*top != NULL) {
        *top = (*top)->next;
    }
    return tmp->data;
}

bool IsEmpty(Stack** top) { return *top == NULL; }

int main()
{
    Stack* top = nullptr;
    std::string str;
    std::getline(std::cin, str);
    str = (std::string)str;

    std::string tok;
    int i = 0;

    while (i < str.length()) {
        while (isspace(str[i])) {
            i++;
        }

        if (isdigit(str[i])) {
            while (isdigit(str[i])) {
                tok += str[i];
                i++;
            }
            Push(&top, atoi(tok.c_str()));
            tok.clear();
        }

        if (str[i] == '*') {
            int a = Pop(&top);
            int b = Pop(&top);
            Push(&top, b * a);
            i++;
        }

        if (str[i] == '+') {
            int a = Pop(&top);
            int b = Pop(&top);
            Push(&top, b + a);
            i++;
        }
        if (str[i] == '-') {
            int a = Pop(&top);
            int b = Pop(&top);
            Push(&top, b - a);
            i++;
        }
    }

    std::cout << top->data << std::endl;
    return 0;
}
