def apply_all_func(int_list, *functions):
    func_dict = {}
    for function in functions:
        function(int_list)
        result = function(int_list)
        func_dict.setdefault(function.__name__, result)
    return func_dict

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))