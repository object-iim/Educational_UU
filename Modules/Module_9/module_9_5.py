# Вторая версия. Работает корректно, но пришлось (не?) значительно поменять требования к заданию

class Iterator:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        if (step > 0 and start > end) or (step < 0 and start < end):
            print("Шаг указан неверно")
            self.stop = True
        else:
            self.stop = False

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.stop:  # Если шаг указан неверно, просто выходим
            raise StopIteration
        if (self.step > 0 and self.current > self.end) or (self.step < 0 and self.current < self.end):
            raise StopIteration
        current_value = self.current
        self.current += self.step
        return current_value


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()


# Первая персия, до изменения ТЗ. Работает, но не корректно

# class StepValueError(ValueError):
#     pass
#
# class Iterator:
#
#     def __init__(self, start, stop, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.pointer = start
#         if step == 0:
#             raise StepValueError('шаг не может быть равен 0')
#
#     def __iter__(self):
#         self.pointer = self.start
#         return self
#
#     def __next__(self):
#         if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
#             raise StopIteration()
#         self.pointer += self.step
#         return self.pointer
#
# try:
#     iter1 = Iterator(100, 200, 0)
#     for i in iter1:
#         print(i, end=' ')
# except StepValueError:
#     print('Шаг указан неверно')
#
# iter2 = Iterator(-5, 1)
# iter3 = Iterator(6, 15, 2)
# iter4 = Iterator(5, 1, -1)
# iter5 = Iterator(10, 1)
#
# for i in iter2:
#     print(i, end=' ')
# print()
# for i in iter3:
#     print(i, end=' ')
# print()
# for i in iter4:
#     print(i, end=' ')
# print()
# for i in iter5:
#     print(i, end=' ')
# print()