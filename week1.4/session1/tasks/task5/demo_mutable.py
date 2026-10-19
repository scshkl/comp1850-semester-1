import copy

def demo_by_ref(data):
    # no good
    # data.append(5)
    # return data

    # still shallow copy
    # data2 = data.copy()
    # data2.append(5)

    # deep copy
    data2 = copy.deepcopy(data)
    data2.append(5)

    return data2

lst_num = [1, 2, 3, 4]
lst_num2 = demo_by_ref(lst_num)
print(lst_num)
print(lst_num2)


def demo_by_value(x):
    x += 5
    return x

# value_x = 10
# value_x2 = demo_by_value(value_x)
# print(value_x)
# print(value_x2)