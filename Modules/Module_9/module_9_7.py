def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        if original_result <= 1:
            result = 'Результат суммы меньше или равен единице'
        else:
            for i in range(2, int(original_result**0.5) + 1):
                if original_result % i == 0:
                    result = 'Составное'
                    break
            else:
                result = 'Простое'
        print(result)
        return original_result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)