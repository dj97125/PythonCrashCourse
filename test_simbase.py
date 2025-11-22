import json
import ssl
import certifi
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Test URL
TEST_URL = "http://89.117.153.222:8080/customState.json"

# Simbase URL
SIMBASE_URL = "https://api.simbase.com/v2/simcards/8910300000003165341/reset"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "live-w2gcfBaxzJ4c2qwDTjFvfwUMm_s8R1JTKPS-PbckgjpEH77uojVlsn7LKhgrzBRMs"
}

def check_test_url():
    try:
        req = Request(TEST_URL)
        with urlopen(req, timeout=10) as response:
            print(f"Test URL HTTP status: {response.status}")
            if response.status == 200:
                print("Test URL returned 200 → skipping Simbase call")
                return True
            else:
                print("Test URL did not return 200 → calling Simbase")
                return False
    except Exception as e:
        print(f"Error checking test URL: {e} → calling Simbase")
        return False

def call_simbase():
    try:
        data = json.dumps({}).encode("utf-8")
        req = Request(SIMBASE_URL, data=data, headers=HEADERS, method="POST")
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        with urlopen(req, timeout=10, context=ssl_context) as response:
            res_body = response.read().decode()
            print(f"Simbase Response Code: {response.status}")
            print(f"Simbase Response Body: {res_body}")
            return response.status, res_body
    except Exception as e:
        print(f"Error calling Simbase: {e}")
        return None, None

if __name__ == "__main__":
    if not check_test_url():
        call_simbase()
