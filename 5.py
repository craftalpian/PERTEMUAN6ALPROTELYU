# # For
# my_attempt = 0
# username = "telkom"
# password = "kampusterbaik"

# for i in range(999):
#     user_input = input("Masukan username: ")
#     pass_input = input("Masukan password: ")

#     if my_attempt >= 3:
#         print("Anda harus reset ke admin")
#         break

#     if user_input == username and pass_input == password:
#         print("Welcome, Bos! Anda telah berhasil login")
#         break
#     else:
#         my_attempt += 1
#         print("Username atau password salah!")

# While
my_attempt = 0
username = "telkom"
password = "kampusterbaik"

while True:
    user_input = input("Masukan username: ")
    pass_input = input("Masukan password: ")

    if my_attempt >= 3:
        print("Anda harus reset ke admin")
        break

    if user_input == username and pass_input == password:
        print("Welcome, Bos! Anda telah berhasil login")
        break
    else:
        my_attempt += 1
        print("Username atau password salah!")