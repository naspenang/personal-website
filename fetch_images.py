import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = {
    "rdms": "https://online.library.uitm.edu.my/rdms/",
    "iclam": "https://online.library.uitm.edu.my/iClam/",
    "era": "https://online.library.uitm.edu.my/Era/",
    "tourbuilder": "https://online.library.uitm.edu.my/TourBuilder/"
}

for name, url in urls.items():
    try:
        r = requests.get(url, timeout=10, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
        print(f"--- {name} ---")
        for img in soup.find_all("img"):
            print(img)
    except Exception as e:
        print(f"Error on {name}: {e}")
