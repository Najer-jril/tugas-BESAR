import json

# Load data pengguna dari file JSON
with open('useroradmin.json', 'r') as file:
    user_data = json.load(file)

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    for user in user_data.get("users", []):
        if user["username"] == username and user["password"] == password:
            print(f"Selamat datang, Anda adalah seorang {user['role']}")
            break
    else:
        print("Username atau password salah. Masukkan dengan benar!!")

if __name__ == "__main__":
    login()
