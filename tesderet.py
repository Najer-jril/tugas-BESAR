import json

# Membuat list untuk menyimpan data pengguna
users = []

# Meminta pengguna untuk memasukkan banyaknya data yang akan dibuat
num_users = int(input("Masukkan banyaknya data yang akan dibuat: "))

# Meminta pengguna untuk memasukkan 6 digit awal yang akan digunakan
input_prefix = input("Masukkan 6 digit awal: ")

# Memeriksa apakah input_prefix memiliki 6 digit
if len(input_prefix) != 6 or not input_prefix.isdigit():
    print("Masukkan harus berupa 6 digit.")
else:
    # Membuat urutan otomatis
    for i in range(1, num_users + 1):
        # Membuat username dengan 6 digit awal + urutan 2 digit terakhir
        username = input_prefix + '{:02d}'.format(i)

        # Membuat dictionary untuk setiap pengguna
        user_data = {
            "username": username,
            "password": username,
            "role": "user"
        }

        # Menambahkan data pengguna ke dalam list
        users.append(user_data)

    # Menyimpan data pengguna dalam file JSON
    with open("user_data.json", "w") as file:
        json.dump(users, file)

    print("Data pengguna telah disimpan dalam user_data.json.")
