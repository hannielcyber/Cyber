
# 🔒 Cybersecurity Python Projects 🚀

This collection contains ** 12 simple scripts** for educational and security testing purposes. Each script focuses on a specific area in cybersecurity — from web security scanning to password strength and brute-force testing.

---

## 1️⃣ HTTP Header Analysis

**Description:**  
A Python script that performs a basic security analysis of HTTP response headers for a given URL.

### 🔍 Features
- ✅ Scans target URLs for important HTTP response headers.
- 🔒 Highlights missing or improperly configured headers.
- Checks for:
  - `X-XSS-Protection`
  - `X-Content-Type-Options`
  - `X-Frame-Options`
  - `Strict-Transport-Security`
  - `Content-Security-Policy`
- 🍪 Analyzes cookie attributes like `Secure` and `HttpOnly`.

### 📦 Requirements
- Python 3.x  
- `requests` library  
  ```bash
  pip install requests
  ```

### 🚀 Usage
1. Open `HTTP_Header_Analysis.py`.  
2. Modify the URL inside the script.
3. Run:  
   ```bash
   python HTTP_Header_Analysis.py
   ```

### 🖥️ Sample Output
```
Response Headers:
- X-Frame-Options : SAMEORIGIN
- X-Content-Type-Options : nosniff

Running Header Security Checks:
- [+] X-XSS-Protection : pass
- [+] X-Content-Type-Options : pass
- [+] X-Frame-Options : pass
- [-] Strict-Transport-Security header not present : fail!
- [-] Content-Security-Policy header not present : fail!

Set-Cookie Checks:
- sessionid=123456
- [+] Secure : pass
- [+] HttpOnly : pass
```

---

## 2️⃣ Password Cracker (Brute-Force using Wordlist)

**Description:**  
A Python script that attempts to recover plaintext passwords by brute-forcing them using a wordlist.

### 🔍 Features
- Supports `sha256`, `md5`, `sha1`, etc.
- Reads and checks each word from a wordlist.
- Shows progress every 1,000 attempts.
- Reports the cracked password and its line number.

### 🧰 Requirements
- Python 3.x  

### ⚙️ Usage
```bash
python password_cracker.py <target_hash> <wordlist_path> [hash_algorithm]
```

| Argument | Description |
|----------------|-----------------|
| `<target_hash>` | The hashed password you want to crack |
| `<wordlist_path>` | Path to `.txt` file |
| `[hash_algorithm]` | Optional (default: sha256) |

### 🧪 Example
```bash
python password_cracker.py 5e88489... wordlist.txt sha256
```

✅ **Sample Output:**
```
[INFO] Using wordlist: wordlist.txt
[INFO] Target hash: 5e88489...
[INFO] Hash algorithm: sha256
[INFO] Starting brute-force attack...
[INFO] Checked 1000 passwords so far...
[SUCCESS] Password found: 'password123' (Line 2035)
```

---

## 3️⃣ Simple XSS Vulnerability Detector

**Description:**  
Tests GET and POST parameters for possible Cross-Site Scripting (XSS) vulnerabilities.

### 🔍 Features
- Tests GET and POST.
- Uses common XSS payloads.
- Highlights vulnerable parameters.

### 🧰 Requirements
- Python 3.x  
- `requests` library  

```bash
pip install requests
```

### ⚙️ Usage
```bash
python Simple_XSS_Vulnerability_Detector.py
```

### 🧪 Example
```
Enter target URL: http://example.com/search?q=test
HTTP method: GET

[*] Testing GET parameters...
Testing parameter: q
[!] Potential XSS vulnerability detected for parameter 'q' with payload:
<script>alert('XSS')</script>
```

---

## 4️⃣ Password Strength Checker

**Description:**  
Evaluates password strength using length and complexity.

### 🚀 Features
- Checks:
  - Minimum 8 characters
  - Lowercase
  - Uppercase
  - Numbers
  - Special characters (@$!%*?&)
- Score out of 5 with suggestions.

### 🧰 Requirements
- Python 3.x  

### ⚙️ Usage
```bash
python PASSWORD_CHECKER.py
```

### 🧪 Example
```
Enter password: Welcome123
Strength Score: 4/5
Suggestions: Add at least one special character.
```

---

## 5️⃣ Password Generator and Checker

**Description:**  
Generates secure random passwords and checks strength.

### 📌 Features
- Randomly generates:
  - Uppercase/lowercase
  - Numbers
  - Special chars
- Checks strength by rules.

### 🧰 Requirements
- Python 3.x  

### ⚙️ Usage
```bash
python PASSWORD_GENERATOR_AND_CHECKER.py
```

### 🧪 Example
```
Password Generator and Strength Checker
Enter length: 12
Generated password: m%5GpZsiK$w3
Strength: Strong.
```

---

## 6️⃣ Simple File Hasher

**Description:**  
Calculates SHA-256 hash of any file.

### 🚀 Features
- SHA-256 hash calculation.

### 🧰 Requirements
- Python 3.x  

### ⚙️ Usage
```bash
python SIMPLE_FILE_HASHER.py
```

Edit:
```python
print("Hash:", file_hash("example.txt"))
```

---

## 7️⃣ Simple Keylogger

**Description:**  
A simple keylogger that saves keystrokes to `keylog.txt` and can email the log.

### 🚀 Features
- Logs keys until ESC.
- Optionally sends log via email.

### 📦 Requirements
- Python 3.x  
- `pynput`

```bash
pip install pynput
```

### ⚙️ Usage
Edit config in `KEYLOGGER.py`:

```python
EMAIL_ADDRESS = "you@example.com"
EMAIL_PASSWORD = "yourpassword"
SEND_TO = "receiver@example.com"
SEND_EMAIL = False  # True to send
```

Run:
```bash
python KEYLOGGER.py
```

---


## 8️⃣ 🔐 Password List Generator
**Description:**  
This project is a simple Python script designed to generate a large list of random lowercase passwords. It is useful for testing password cracking tools, brute-force simulations, or other cybersecurity-related experiments.

---

### 📜 Features

- ✅ Generates **1 million** random passwords  
- ✅ Each password:
  - Is **8 characters** long  
  - Consists of **lowercase letters only** (`a-z`)  
- ✅ Outputs the list to a file named `password.lst`

---

### 🧰 Requirements

- Python **3.x**  
- No external libraries needed (uses built-in `random` and `string` modules)

---

### 🏃‍♂️ Usage

1. Clone or download this project.
2. Run the script using Python:

   ```bash
   python PASSWORD\ LIST\ GENERATOR.py
   ```

3. A file named `password.lst` will be created in the same directory containing **1 million** randomly generated passwords.

---

### 📁 Output Example

Each line in `password.lst` contains one 8-character password. Example:

```
qweorplk
zmxnvcas
asldkfjg
...
```

 ## 9️⃣🔐 Simple Password Hasher (C)
**Description:**



This project is a simple C program that demonstrates how to hash and verify passwords using the **SHA-256** algorithm from the OpenSSL library. It simulates a basic password authentication mechanism.

---

### 📜 Features

- Hashes user input using **SHA-256**
- Compares hashed input against a stored hash (for password: `secret123`)
- Provides simple feedback: `Access Granted ✅` or `Access Denied ❌`
- Uses OpenSSL's cryptographic functions

---

### 🧰 Requirements

- GCC or any standard C compiler
- OpenSSL development libraries (`libssl-dev` or equivalent)

---

### 🏗️ Build Instructions

To compile the program, use:

```bash
gcc SIMPLE_PASSWORD_HASHER.c -o password_hasher -lssl -lcrypto
```

---

### 🚀 Usage

Run the program after compiling:

```bash
./password_hasher
```

Then enter a password when prompted. The program will hash your input and compare it to a stored hash (for `"secret123"`).

---

### 🧪 Sample Output

```
Enter your password: secret123
Hashed password: 2bb80d537b1da3e38bd30361aa855686bde0ba28a5a...

Access Granted ✅
```

---

## 🔟  🛡️ File Integrity Checker
**Description:**




A lightweight Python script to monitor changes in any file by checking its SHA-256 hash over time. Useful for detecting unauthorized modifications, ensuring data integrity, and protecting against tampering.

### 📂 Overview

This script continuously monitors a specified file and alerts you when its content changes by comparing its cryptographic hash.

### 🔧 Features

- Calculates SHA-256 hash of any file
- Continuously monitors the file at regular intervals
- Sends an alert if a change is detected
- Simple and efficient, no external dependencies

### 🧪 How It Works

1. The script computes the SHA-256 hash of the file initially.
2. At a defined interval (default: 10 seconds), it recalculates the hash.
3. If the new hash differs from the original, a warning is triggered.

### 📦 Requirements

- Python 3.x

No additional libraries are required — it uses the built-in `hashlib`, `os`, and `time` modules.

### 🚀 Usage

1. Clone or download this repository.
2. Replace the placeholder path with the file you want to monitor:

```python
if __name__ == "__main__":
    file_to_monitor = "path/to/your/file.txt"  # Update this line
    monitor_file(file_to_monitor)
```

3. Run the script:

```bash
python FILE\ INTEGRITY\ CHECKER.py
```

4. You'll see regular updates in the terminal. If the file is modified, the script will alert you.

### 🧪 Sample Output

```
Monitoring path/to/your/file.txt. Initial hash: 1234abcd...
No changes detected. Current hash: 1234abcd...
ALERT! File path/to/your/file.txt has been modified.
Original hash: 1234abcd...
Current hash: 5678efgh...
```

### 📌 Notes

- This script halts after detecting a single change. You can modify it to continue monitoring if needed.
- Ensure the file path is correct and accessible by the script.



## 1️⃣1️⃣ 🔍 Go Port Scanner
**Description:**




A simple and fast port scanner written in Go. Useful for learning basic network scanning concepts and Go's concurrency model.

### 📦 Features

- Scans a given IP or hostname
- Supports a custom range of ports
- Displays open ports only
- Fast scanning using goroutines

### 📦 Requirements
- Go 1.13+

### 🚀 Usage


1.  Run the scanner

```bash
go run port_scanner.go
```

 2.  📥Input

You will be prompted to enter:
- Hostname or IP (e.g., `scanme.nmap.org`)
- Start port (e.g., `1`)
- End port (e.g., `1024`)

### 🧪 Sample Output

```bash
Enter hostname or IP to scan: scanme.nmap.org
Enter start port: 20
Enter end port: 100
Open ports:
 - 22
 - 80
```



 ## 1️⃣2️⃣🔐 Encryption & Decryption Toolkit

This project provides simple command-line tools for **text encryption and decryption** using three classic cipher techniques:  

- **Caesar Cipher**  
- **XOR Cipher**  
- **Vigenère Cipher**  

The toolkit is split into two scripts:  

- `ENCRYPTION_TOOL.py` → Encrypts plaintext into ciphertext.  
- `DECRYPTION_TOOL.py` → Decrypts ciphertext back into plaintext.  

---

### 🚀 Features

- Interactive command-line interface.  
- Supports **three different cipher algorithms**.  
- Input validation (keys must match expected format).  
- Works with uppercase and lowercase letters.  
- Lightweight — no external dependencies required.  

---

### 📂 Project Structure

```
📁 Encryption-Decryption-Toolkit
 ├── ENCRYPTION_TOOL.py   # Encrypts text
 ├── DECRYPTION_TOOL.py   # Decrypts text
 └── README.md            # Project documentation
```

---

### ⚙️ Installation

1. Clone or download the project folder.  
2. Ensure you have **Python 3.x** installed on your system.  
3. Run the scripts directly with Python:

```bash
python ENCRYPTION_TOOL.py
python DECRYPTION_TOOL.py
```

---

### 🛠️ Usage

### 1. Encryption
Run the encryption tool:

```bash
python ENCRYPTION_TOOL.py
```

Steps:
1. Choose a cipher method:  
   - `1` → Caesar Cipher  
   - `2` → XOR Cipher  
   - `3` → Vigenère Cipher  
2. Enter the text you want to encrypt.  
3. Provide the encryption key depending on the cipher.  
4. The encrypted text is displayed.  

---

### 2. Decryption
Run the decryption tool:

```bash
python DECRYPTION_TOOL.py
```

Steps:
1. Choose the cipher method used during encryption.  
2. Enter the encrypted text.  
3. Provide the decryption key (must match the encryption key).  
4. The decrypted text is displayed.  

---

## 🔑 Cipher Details

### Caesar Cipher
- Shifts each letter by a numeric key.  
- Example: `"HELLO"` with key `3` → `"KHOOR"`.  

### XOR Cipher
- Applies bitwise XOR with a numeric key (`1–255`).  
- Symmetric: encryption and decryption use the same operation.  

### Vigenère Cipher
- Uses a keyword of letters to determine shifting for each character.  
- Example: Text `"HELLO"`, Key `"KEY"` → `"RIJVS"`.  

---

## 📌 Example Workflow

**Encryption (Caesar Cipher):**
```
=== ENCRYPTION TOOL ===
Choose a cipher method:
1. Caesar Cipher
2. XOR Cipher
3. Vigenère Cipher

Enter your choice (1-3): 1
Enter the text to encrypt: HELLO
Enter the shift key (number): 3

Original text: HELLO
Caesar key: 3
Encrypted text: KHOOR
```

**Decryption (Caesar Cipher):**
```
=== DECRYPTION TOOL ===
Choose the cipher method used for encryption:
1. Caesar Cipher
2. XOR Cipher
3. Vigenère Cipher

Enter your choice (1-3): 1
Enter the encrypted text: KHOOR
Enter the shift key used for encryption: 3

Encrypted text: KHOOR
Caesar key: 3
Decrypted text: HELLO
```

---






















## ⚠️ DISCLAIMER

For educational & ethical use only. Use responsibly with permission!
