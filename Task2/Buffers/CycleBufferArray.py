class CycleBufferArray:

    def __init__(self, size):
        self._buffer = [None] * size
        self._size = size
        self._count = 0

    def _cycle_shift(self):
        self._buffer = self._buffer[-1:] + self._buffer[:-1]

    def enqueue(self, item):
        self._cycle_shift()
        self._buffer[0] = item
        if self._count < self._size:
            self._count += 1

    def dequeue(self):
        ans = self.pic()
        self._buffer[self._count - 1] = None
        self._count -= 1
        return ans

    def is_empty(self):
        if self._count == 0:
            return True
        return False

    def pic(self):
        if self.is_empty():
            return None
        return self._buffer[self._count - 1]

# Буффер написан на массиве
# Асимптотическая оценка по времени
# enqueue - O(n) (операции из циклического сдвига работают за O(n))
# dequeue - O(1)
# is_empty - O(1)
# pic - O(1)
# Плюсы: Прост в реализации
# Минусы: Доставать элемент за линейную асмптоику - достаточно медленно
#         За счет массива, объекты расположены в памяти подряд, но этот факт в структуре не используется,
#         а значит мы расходуем потенциально полезную непрерывную память
