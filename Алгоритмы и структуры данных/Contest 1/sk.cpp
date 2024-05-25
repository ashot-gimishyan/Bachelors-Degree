#include <iostream>

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
    int ch;
    bool is_good = true;

    while (true) {

        ch = getchar();
        if (ch == '\n')
            break;
        // если скобка открывающая, то кладем в стек
        if (ch == '(' || ch == '[' || ch == '{')
            Push(&top, ch);

        else if (ch == ')' || ch == ']' || ch == '}') {
            if (IsEmpty(&top)) {
                is_good = false;
                break;
            }

            int open_bracket = Pop(&top);
            if (open_bracket == '(' && ch == ')')
                continue;
            if (open_bracket == '[' && ch == ']')
                continue;
            if (open_bracket == '{' && ch == '}')
                continue;

            is_good = false;
            break;
        }
    }

    if (is_good && IsEmpty(&top))
        std::cout << "YES" << std::endl;
    else
        std::cout << "NO" << std::endl;
}
