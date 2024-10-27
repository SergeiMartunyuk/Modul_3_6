def calculate_structure_sum(numb):
    summ_ = 0
    if isinstance(numb, (list, tuple, set)):
        for i in numb:
            summ_ += calculate_structure_sum(i)
    elif isinstance(numb, dict):
        for i in numb.values():
            summ_ += i
        for i in numb.keys():
                keys_ = i
                summ_ += len(keys_)
    elif isinstance(numb, str):
        summ_ += len(numb)
    elif isinstance(numb, int):
        summ_ += numb
    return summ_

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)