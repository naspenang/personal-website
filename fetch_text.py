import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    "https://online.library.uitm.edu.my/rdms/",
    "https://online.library.uitm.edu.my/iClam/",
    "https://online.library.uitm.edu.my/Era/",
    "https://online.library.uitm.edu.my/TourBuilder/"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for url in urls:
    try:
        r = requests.get(url, headers=headers, timeout=10, verify=False)
        print(f"--- {url} --- STATUS: {r.status_code}")
        srcs = re.findall(r'src=[\'"]([^\'"]+)[\'"]', r.text)
        for p in srcs:
            if any(p.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.ico']):
                print("FOUND:", p)
    except Exception as e:
        print(f"Error on {url}: {e}")
