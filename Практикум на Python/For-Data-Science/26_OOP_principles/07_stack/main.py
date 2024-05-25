class Stack:
    def __init__(self):
        self.__buffer = list()

    def __str__(self):
        return '; '.join(self.__buffer)

    def push(self, element):
        self.__buffer.append(element)

    def pop(self):
        if len(self.__buffer) == 0:
            return None
        return self.__buffer.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for key in sorted(self.task.keys()):
                display.append('{} {}\n'.format(str(key), self.task[key]))
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
