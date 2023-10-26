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

# Data input
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Output hasil
for item in data:
    extracted_data = extract_digits(item)
    print(extracted_data)
