import random
import string

charset = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
length = 8
num_passwords = 1_000_000  # 1 million

with open('password.lst', 'w') as f:
    for _ in range(num_passwords):
        password = ''.join(random.choices(charset, k=length))
        f.write(password + '\n')

print(f"Generated {num_passwords} passwords in 'password.lst'")
