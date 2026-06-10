import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    "https://online.library.uitm.edu.my/rdms/",
    "https://online.library.uitm.edu.my/iClam/",
    "https://online.library.uitm.edu.my/Era/",
    "https://online.library.uitm.edu.my/TourBuilder/"
]

for url in urls:
    try:
        r = requests.get(url, timeout=10, verify=False)
        print(f"--- {url} ---")
        links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', r.text)
        srcs = re.findall(r'src=[\'"]([^\'"]+)[\'"]', r.text)
        styles = re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', r.text)
        
        for p in links + srcs + styles:
            if any(p.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.ico']):
                print("FOUND:", p)
    except Exception as e:
        print(f"Error on {url}: {e}")
