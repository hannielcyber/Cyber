import hashlib

def file_hash(path):
    with open(path, 'rb') as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

print("Hash:", file_hash("example.txt"))
