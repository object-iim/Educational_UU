my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

inception = 0

while inception < len(my_list):
    num = my_list[inception]
    inception = inception + 1
    if num == 0:
        continue
    if num < 0:
        print("Конец")
        break
    elif inception == len(my_list):
        break
    elif num > 0:
        print(num)