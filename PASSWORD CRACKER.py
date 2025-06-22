import hashlib
import sys
import os

def hash_password(password, algorithm='sha256'):
    """Hash the password using the specified algorithm."""
    try:
        hash_func = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    
    hash_func.update(password.encode('utf-8'))
    return hash_func.hexdigest()

def brute_force_password(target_hash, wordlist_path, algorithm='sha256'):
    """Attempts to find the password by hashing each word in the wordlist."""
    if not os.path.isfile(wordlist_path):
        print(f"[ERROR] Wordlist file not found: {wordlist_path}")
        return None

    print(f"\n[INFO] Using wordlist: {wordlist_path}")
    print(f"[INFO] Target hash: {target_hash}")
    print(f"[INFO] Hash algorithm: {algorithm}")
    print("[INFO] Starting brute-force attack...\n")

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_number, word in enumerate(f, start=1):
                word = word.strip()
                hashed = hash_password(word, algorithm)
                if hashed == target_hash:
                    print(f"\n[SUCCESS] Password found: '{word}' (Line {line_number})")
                    return word

                if line_number % 1000 == 0:
                    print(f"[INFO] Checked {line_number} passwords so far...")

    except Exception as e:
        print(f"[ERROR] Failed to read or process the wordlist: {e}")
        return None

    print("\n[FAILURE] Password not found in wordlist.")
    return None

def main():
    if len(sys.argv) not in [3, 4]:
        print("\nUsage: python password_cracker.py <target_hash> <wordlist_path> [hash_algorithm]")
        print("Example: python password_cracker.py 5e88489... wordlist.txt sha256")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist_path = sys.argv[2]
    algorithm = sys.argv[3].lower() if len(sys.argv) == 4 else 'sha256'

    if algorithm not in hashlib.algorithms_guaranteed:
        print(f"[ERROR] Unsupported hash algorithm: {algorithm}")
        print(f"[INFO] Supported algorithms: {', '.join(sorted(hashlib.algorithms_guaranteed))}")
        sys.exit(1)

    brute_force_password(target_hash, wordlist_path, algorithm)

if __name__ == "__main__":
    main()
