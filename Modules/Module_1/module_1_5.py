immutable_var = 3, 2, 1, False, "dreams"
print(immutable_var)

# Мы не можем изменить элементы кортежа, т.к. этим кортеж и отличается от списков (кроме того, что занимает меньше места)
# Если мы попытаемся ихменить кортеж и введем immutable_varp[4] = 'life' то на этом этапе программа выдаст ошибку и остановит чтение кода

mutable_list = ['a', 'd,', 'c']
mutable_list[1] = 'b'
print(mutable_list)