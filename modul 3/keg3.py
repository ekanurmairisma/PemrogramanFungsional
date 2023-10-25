random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

def process_int(item):
    satuan = item % 10
    puluhan = (item % 100) // 10
    ratusan = item // 100
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

def is_float(item):
    return isinstance(item, float)

def is_string(item):
    return isinstance(item, str)

# map dan filter untuk memproses data
int_dict = dict(map(lambda item: (item, process_int(item)), filter(lambda item: isinstance(item, int), random_list)))
float_tuple = tuple(filter(is_float, random_list))
str_list = list(filter(is_string, random_list))

print("\nData Float:")
print(float_tuple)

print("\nData Int:")
for key, value in int_dict.items():
    print(value)

print("\nData String:")
print(str_list)
