


1. HTTP Header Analysis



This project is a Python script that performs a basic security analysis of HTTP response headers for a given URL. 
It checks for the presence and correct configuration of several essential HTTP security headers to help improve the security posture of web applications.
--------------------------------------------------------------------------------------------------------------------------------------

🔍 Features

✅ Scans target URLs for important HTTP response headers.

🔒 Highlights missing or improperly configured headers that can expose your web application to attacks.
- Checks for the following security headers:
  - `X-XSS-Protection`
  - `X-Content-Type-Options`
  - `X-Frame-Options`
  - `Strict-Transport-Security`
  - `Content-Security-Policy`

🍪 Analyzes cookie attributes like Secure and HttpOnly.
--------------------------------------------------------------------------------------------------------------------
📦 Requirements

- Python 3.x
- `requests` library

Install the required package using pip: pip install requests
----------------------------------------------------------------------------------------- 
🚀 Usage
i. Open the script HTTP Header Analysis.py.

ii. Modify the URL inside the main block to the desired target:


url = "http://localhost:8000/setup.php"

iii. Run the script:
python "HTTP Header Analysis.py"
-------------------------------------------------------------------------------------------
🖥️ Sample Output


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


---------------------------------------------------------------------------------------------------------------------------------
2. 🔐 Password Cracker (Brute-Force using Wordlist)

This Python script attempts to recover plaintext passwords by "brute-forcing" them using a "wordlist" and comparing the hashes.
It supports various hashing algorithms and is useful for educational purposes, security testing, and understanding password vulnerabilities.

--------------------------------------------------------------------------------------------------------------------------------------
🔍 Features

- Supports common hashing algorithms (`sha256`, `md5`, `sha1`, etc.)
- Reads and checks each word from a wordlist file
- Gracefully handles errors like missing files or unsupported algorithms
- Reports success with line number and password if found
- Displays progress every 1000 attempts (can be modified)
-------------------------------------------------------------------------------------------------------------
🧰 Requirements

- Python 3.x
- No third-party packages required (uses Python's standard library)
----------------------------------------------------------------------------------------------------------------
⚙️ Usage

``bash
python password_cracker.py <target_hash> <wordlist_path> [hash_algorithm]


🔸 Arguments

| Argument           | Description                                |
| ------------------ | ------------------------------------------ |
| `<target_hash>`    | The hashed password you want to crack      |
| `<wordlist_path>`  | Path to a `.txt` file containing passwords |
| `[hash_algorithm]` | Optional. Default is `sha256`              |
------------------------------------------------------------------------------------------------------------------
🧪 Example
python password_cracker.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd  wordlist.txt sha256



✅ Sample Output
- [INFO] Using wordlist: wordlist.txt
- [INFO] Target hash: 5e88489...
- [INFO] Hash algorithm: sha256
= [INFO] Starting brute-force attack...

- [INFO] Checked 1000 passwords so far...
- [INFO] Checked 2000 passwords so far...

- [SUCCESS] Password found: 'password123' (Line 2035)


---------------------------------------------------------------------------------------------------------------
3. Simple XSS Vulnerability Detector
   
This Python script is designed to detect Cross-Site Scripting (XSS) vulnerabilities in web applications by testing both GET and POST parameters with common XSS payloads.
It helps identify potential security flaws where user input might be improperly sanitized.
----------------------------------------------------------------------------------------------------------
🔍 Features
- Tests both GET and POST request parameters
- Uses a variety of common XSS payloads
- Provides detailed output of vulnerable parameters
- Simple command-line interface 
-------------------------------------------------------------------------------------------------------------------
🧰 Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)
----------------------------------------------------------------------------------------------------------------------
⚙️ Usage
- Run the script:  `python Simple_XSS_Vulnerability_Detector.py` 
- Enter the target URL when prompted (include parameters for GET testing)
- Select the HTTP method to test (GET or POST)
- For POST requests, you'll be prompted to enter parameters in key=value format
-----------------------------------------------------------------------------------------------------------------------------
🧪 Example


== Simple XSS Vulnerability Detector ===

- Enter target URL (include parameters for GET testing): http://example.com/search?q=test
- HTTP method to test (GET or POST): GET

- [*] Testing GET parameters for XSS injection...

- Testing parameter: q
-   [!] Potential XSS vulnerability detected for parameter 'q' with payload:
      <script>alert('XSS')</script>

- Summary of potential vulnerabilities found:
-  Parameter: q
-  Payload: <script>alert('XSS')</script>
-  URL: http://example.com/search?q=test<script>alert('XSS')</script>

=== Test completed ===
--------------------------------------------------------------------------------------------
4. 🔐 Password Strength Checker
   
This Python script evaluates the strength of a given password based on five key criteria and offers suggestions to improve it.
-------------------------------------------------------------------------------------
🚀 Features
- Checks password length (minimum 8 characters)

- Verifies the presence of:

✅ Lowercase letters

✅ Uppercase letters

✅ Numbers

✅ Special characters (@$!%*?&)

- Returns a strength score out of 5

- Provides feedback and improvement suggestions
---------------------------------------------------------------------------------------------
🧠 How It Works



The password is analyzed using regular expressions. For every criterion met, a point is added to the strength score. If a criterion is not met, a helpful suggestion is displayed.

----------------------------------------------------------------------------------------------------------

🧰 Requirements


Python 3.x (no external libraries required)


------------------------------------------------------------------------------------------------------------------
⚙️ Usage



Run the script:python PASSWORD\ CHECKER.py


Input a password when prompted.



Receive a strength score and suggestions.


-------------------------------------------------------------------------------------------------------------

🧪Example Output


Enter your password: Welcome123


Password Strength Score: 4/5



Suggestions for improvement:



- Add at least one special character (e.g., @$!%*?&).


--------------------------------------------------------------------------------------------------------------------
5. 🔐 Password Generator and Strength Checker



This Python script allows you to generate a secure random password and evaluate its strength based on common security criteria.
-------------------------------------------------------------------------------------------------------------------------
📌 Features
🔄 Randomly generates passwords with:

- Uppercase and lowercase letters

- Numbers

- Special characters

✅ Checks password strength with clear feedback


🔒 Validates length and complexity

---------------------------------------------------------------------------------------------------------------
🧠 How It Works
- User inputs a desired password length.

- The script generates a random password of that length.
- It evaluates the password's strength using predefined rules.

--------------------------------------------------------------------------------------------------------------
🦾Strength Criteria

| Condition                    | Strength  |
| ---------------------------- | --------- |
| < 8 characters               | Very weak |
| Only letters or digits       | Weak      |
| Letters and digits only      | Medium    |
| Letters, digits, and symbols | Strong    |


--------------------------------------------------------------------------------------------------------------------
🧰 Requirements
- Python 3.x

- Uses only standard libraries: `random` and `string`
---------------------------------------------------------------------------------------------------------
💻 Usage

 
 Run the Script: python `PASSWORD GENERATOR AND CHECKER.py`

--------------------------------------------------------------------------------------------------------------------------


 🧪Example Output


 Password Generator and Strength Checker
---------------------------------------


Enter the desired password length: 12


Generated password: m%5GpZsiK$w3


Strength: Strong. 


Password contains a blend of numbers, characters, and special characters.
----------------------------------------------------------------------------------------------------------

6. 🧮 Simple File Hasher


This Python script computes the SHA-256 hash of a specified file. It's useful for checking file integrity or verifying data against known hashes.


-------------------------------------------------------------------------------------------------------------

🚀 Features
- Calculates `SHA-256`  hash of any file

- Simple and easy-to-use

- Uses only built-in Python libraries
---------------------------------------------------------------------------------------------------------
🧠 How It Works
- Reads the entire content of the file in binary mode.

- Computes the SHA-256 hash using Python’s `hashlib` module.

- Prints the resulting hexadecimal hash.
------------------------------------------------------------------------------------------------
📦 Requirements
- Python 3.x

- No external libraries needed
-----------------------------------------------------------------------------------------------------------------------------------
 ⚙️Usage


 
i. Prepare a file to hash



Ensure a file like `example.txt` is in the same directory as the script or specify a valid path.




ii. Run the script: python `SIMPLE FILE HASHER.py`



The script will compute and print the hash of example.txt.

⚠️ Note
---------------------------------
To compute the hash of a different file, modify this line:



print("Hash:", file_hash("example.txt"))




Replace `example.txt` with the path to your desired file.

-------------------------------------------------------------------------------------------------------

7.🔐 Keylogger 



This is a simple keylogger implemented in Python using the `pynput` library. It captures keystrokes, logs them to a file, and can optionally send the log via email when the user presses the ESC key.

---------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Features
- Records all keystrokes into `keylog.txt`.

- Stops logging on pressing the ESC key.

- Optional feature to email the log file to a specified address.
--------------------------------------------------------------------------------
📦Requirements
- Python 3.x
- pynput library


Install dependencies with:`pip install pynput`


----------------------------------------------------------------------------------------------------------------
 ⚙️Usage



 
Edit the Configuration: Open `KEYLOGGER.py` and set the following:

EMAIL_ADDRESS = "youremail@example.com"


EMAIL_PASSWORD = "yourpassword"



SEND_TO = "destination@example.com"


SEND_EMAIL = False  # Set to True if you want logs to be emailed

-------------------------------------------------------------------------------------------------------

Run the Script: python `KEYLOGGER.py`




The script will start logging keys. To stop and (optionally) email the log, press ESC.

--------------------------------------------------------------------------------------------------------

Log File



Logged keystrokes are saved to a file named: `Keylog.txt`

-----------------------------------------------------------------------------------------------------------------
Emailing the Log (Optional)

- To enable log emailing:`Set SEND_EMAIL = True`.

- Use a valid SMTP-supported email (Gmail, Outlook, etc.).

  

You may need to enable "Less secure app access" or generate an app password (especially for Gmail).

