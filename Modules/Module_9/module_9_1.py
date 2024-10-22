def apply_all_func(int_list: list, *functions):
    results = {}
    for function in functions:
        a = function.__name__
        b = function(int_list)
        results.update({a: b})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))