import requests

class ScanHeaders:
    def __init__(self, url):
        self.url = url
        try:
            response = requests.get(self.url)
            self.headers = response.headers
            self.cookies = response.cookies
        except requests.exceptions.RequestException as e:
            print(f"[!] Error fetching URL: {e}")
            self.headers = {}
            self.cookies = []

    def scan_xxss(self):
        if "X-XSS-Protection" in self.headers:
            print("[+]", "X-XSS-Protection", ':', "pass")
        else:
            print("[-]", "X-XSS-Protection header not present", ':', "fail!")

    def scan_nosniff(self):
        if self.headers.get("X-Content-Type-Options", "").lower() == "nosniff":
            print("[+]", "X-Content-Type-Options", ':', "pass")
        else:
            print("[-]", "X-Content-Type-Options header not set correctly", ':', "fail!")

    def scan_xframe(self):
        val = self.headers.get("X-Frame-Options", "").lower()
        if val in ["deny", "sameorigin"]:
            print("[+]", "X-Frame-Options", ':', "pass")
        elif val:
            print("[-]", "X-Frame-Options header not set correctly", ':', "fail!")
        else:
            print("[-]", "X-Frame-Options header not present", ':', "fail!")

    def scan_hsts(self):
        if "Strict-Transport-Security" in self.headers:
            print("[+]", "Strict-Transport-Security", ':', "pass")
        else:
            print("[-]", "Strict-Transport-Security header not present", ':', "fail!")

    def scan_policy(self):
        if "Content-Security-Policy" in self.headers:
            print("[+]", "Content-Security-Policy", ':', "pass")
        else:
            print("[-]", "Content-Security-Policy header not present", ':', "fail!")

    def scan_secure(self, cookie):
        if cookie.secure:
            print("[+]", "Secure", ':', "pass")
        else:
            print("[-]", "Secure attribute not set", ':', "fail!")

    def scan_httponly(self, cookie):
        raw_cookie = str(cookie)
        if "httponly" in raw_cookie.lower():
            print("[+]", "HttpOnly", ':', "pass")
        else:
            print("[-]", "HttpOnly attribute not set", ':', "fail!")


if __name__ == "__main__":
    url = "http://localhost:8000/setup.php"
    target = ScanHeaders(url)

    if target.headers:
        print("Response Headers:")
        for key, val in target.headers.items():
            print(key, ":", val)

        print("\nRunning Header Security Checks:\n")
        target.scan_xxss()
        target.scan_nosniff()
        target.scan_xframe()
        target.scan_hsts()
        target.scan_policy()

        if target.cookies:
            print("\nSet-Cookie Checks:")
            for cookie in target.cookies:
                print(f"- {cookie.name}={cookie.value}")
                target.scan_secure(cookie)
                target.scan_httponly(cookie)
        else:
            print("\nNo cookies found.")
