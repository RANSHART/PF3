# Data list seperti pada kegiatan 1 modul 1
random_list = [3.1, 2.7, 105, 7.3, 42, "Hello", "Python", "world", "AI"]

# Filter untuk memisahkan nilai float, int, dan string
filtered_float = list(filter(lambda x: isinstance(x, float), random_list))
filtered_int = list(filter(lambda x: isinstance(x, int), random_list))
filtered_string = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_units(num):
    ratusan = num // 100
    puluhan = (num // 10) % 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

mapped_int = list(map(map_int_to_units, filtered_int))

# Output
print("Data Float:")
print(filtered_float)
print("Data Int:")
for item in mapped_int:
    print(item)
print("Data String:")
print(filtered_string)
