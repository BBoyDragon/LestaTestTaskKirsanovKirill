class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CycleBufferLinkedList:
    def __init__(self, size):
        self._head = None
        self._tail = None
        self._size = size
        self._count = 0
        self._initialize(size)

    def _initialize(self, size):
        self._head = Node()
        current = self._head
        for i in range(size - 1):
            new_node = Node()
            current.next = new_node
            current = new_node
        current.next = self._head
        self._tail = self._head

    def enqueue(self, item):
        if self._count == self._size:
            self._head = self._head.next
        else:
            self._count += 1

        self._tail.data = item
        self._tail = self._tail.next

    def dequeue(self):
        if self.is_empty():
            return None
        data = self._head.data
        self._head.data = None
        self._head = self._head.next
        self._count -= 1
        return data

    def is_empty(self):
        return self._count == 0

    def pic(self):
        if self.is_empty():
            return None
        return self._head.data

# Буффер написан на Связном списке
# Асимптотическая оценка по времени
# enqueue - O(1)
# dequeue - O(1)
# is_empty - O(1)
# pic - O(1)
# инициализация - O(N) - инициализирует набор пустых нод
# Плюсы: Все операции работают за константную асимптотику,
# что достигается за счет потери времени на инициализацию и идее связного списка
#        За счет связного списка мы получаем возможность хранить объекты в разных частях памяти
# Минусы: Сложнее в реализации, чем на массиве
