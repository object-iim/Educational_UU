def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # не работает, ничего не возвращает

inner_function() # ошибка «name 'inner_function' is not defined»

test_function() # работает