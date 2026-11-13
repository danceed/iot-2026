def sum_two_min(numbers):
    first_min, second_min, *rest_sequence = numbers

    if first_min > second_min:
        first_min, second_min = second_min, first_min


    for number in rest_sequence:
        if number < first_min:
            second_min = first_min
            first_min = number
        elif number < second_min:
            second_min = number

    return first_min + second_min

numbers = [19, 5, 42, 2, 77]
numbers2 = [10, 343445353, 3453445, 3453545353453] 

result = sum_two_min(numbers)
result2 = sum_two_min(numbers2)

print("Сума двох мінімальних чисел:", result)
print("Сума двох мінімальних чисел:", result2)