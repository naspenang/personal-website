import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = {
    "rdms": "https://online.library.uitm.edu.my/rdms/",
    "iclam": "https://online.library.uitm.edu.my/iClam/",
    "era": "https://online.library.uitm.edu.my/Era/",
    "tourbuilder": "https://online.library.uitm.edu.my/TourBuilder/"
}

images_dir = r"d:\_ASSISTANTS\COURSES\SEM_4\IML254\projects\personal_website\images"

for name, url in urls.items():
    try:
        r = requests.get(url, timeout=10, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
        
        logo_img = None
        for img in soup.find_all("img"):
            src = img.get("src", "").lower()
            alt = img.get("alt", "").lower()
            cls = " ".join(img.get("class", [])).lower()
            if "logo" in src or "logo" in alt or "logo" in cls:
                logo_img = img
                break
                
        if logo_img:
            img_src = logo_img["src"]
            img_url = urllib.parse.urljoin(url, img_src)
            img_ext = os.path.splitext(img_src.split("?")[0])[1]
            if not img_ext:
                img_ext = ".png"
            dest = os.path.join(images_dir, f"{name}_logo{img_ext}")
            
            img_data = requests.get(img_url, verify=False).content
            with open(dest, "wb") as f:
                f.write(img_data)
            print(f"Downloaded logo for {name}: {dest}")
        else:
            print(f"No logo found for {name}")
    except Exception as e:
        print(f"Error on {name}: {e}")
