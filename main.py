# Fungsi untuk memeriksa apakah karakter adalah angka
def is_digit(char):
    return char.isdigit()

# Fungsi untuk mengambil nilai integer dari setiap data
def extract_digits(data_str):
    digits = []
    current_digit = ""
    for char in data_str:
        if is_digit(char):
            current_digit += char
        elif current_digit:
            digits.append(current_digit)
            current_digit = ""
    if current_digit:
        digits.append(current_digit)
    return digits

# Fungsi untuk mengkonversi minggu, hari, dan jam menjadi menit
def convert_to_minutes(data_str):
    extracted_data = extract_digits(data_str)
    weeks = int(extracted_data[0])
    days = int(extracted_data[1])
    hours = int(extracted_data[2])
    minutes = int(extracted_data[3])
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
    return total_minutes

# Data input
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Output hasil
output_data = []
for item in data:
    converted_minutes = convert_to_minutes(item)
    output_data.append(converted_minutes)

print(output_data)
