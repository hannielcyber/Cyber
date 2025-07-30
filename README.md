
# 🔒 Cybersecurity Python Projects 🚀

This collection contains ** 9 simple scripts** for educational and security testing purposes. Each script focuses on a specific area in cybersecurity — from web security scanning to password strength and brute-force testing.

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

###📜 Features

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


























## ⚠️ DISCLAIMER

For educational & ethical use only. Use responsibly with permission!
