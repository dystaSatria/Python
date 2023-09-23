
import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Masukkan panjang kata sandi yang diinginkan: "))

password = generate_password(length)
print("Kata sandi acak Anda adalah:", password)
