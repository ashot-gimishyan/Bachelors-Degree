#include <cstring>
#include <iostream>

struct Stack {
  int data;
  int min;
  Stack* next;
};

void Push(Stack** top, int n) {
  Stack* st = new Stack();
  st->data = n;
  if (*top == NULL) {
    *top = st;
    (**top).min = n;
  } else {
    st->min = ((n <= (**top).min) ? n : (**top).min);
    st->next = *top;
    *top = st;
  }
  std::cout << "ok" << std::endl;
}

int Back(Stack** top) {
  if (*top == NULL) {
    std::cout << "error" << std::endl;
    return 1;
  }
  std::cout << (**top).data << std::endl;
  return 0;
}

void Pop(Stack** top) {
  if (*top != NULL) {
    std::cout << (**top).data << std::endl;
    *top = (*top)->next;
  } else {
    std::cout << "error" << std::endl;
  }
}

bool IsEmpty(Stack** top) { return *top == NULL; }

int Size(Stack** top) {
  int count = 0;
  Stack* current = *top;
  while (current != NULL) {
    ++count;
    current = current->next;
  }
  return (count);
}

void Clear(Stack** top) {
  while (IsEmpty(top) != true) {
    *top = (*top)->next;
  }
  std::cout << "ok" << std::endl;
}

int Min(Stack** top) {
  if (*top == NULL) {
    std::cout << "error" << std::endl;

    return 1;
  }

  std::cout << (**top).min << std::endl;
  return 0;
}

int main() {
  Stack* top = nullptr;
  int m;
  std::cin >> m;
  std::string str;

  for (int i = 0; i < m; ++i) {
    std::cin >> str;
    if (str == "push") {
      int value;
      std::cin >> value;
      Push(&top, value);
    }
    if (str == "pop") {
      Pop(&top);
    }
    if (str == "back") {
      Back(&top);
    }
    if (str == "min") {
      Min(&top);
    }
    if (str == "size") {
      int res = Size(&top);
      std::cout << res << std::endl;
    }
    if (str == "clear") {
      Clear(&top);
    }
  }
}
