import requests
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

images = {
    "rdms_logo_new.png": "https://online.library.uitm.edu.my/rdms/Images/rdms_light.png",
    "iclam_logo_new.png": "https://online.library.uitm.edu.my/iClam/Images/logo.png",
    "era_logo_new.ico": "https://online.library.uitm.edu.my/Era/Images/favicon.ico"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

images_dir = r"d:\_ASSISTANTS\COURSES\SEM_4\IML254\projects\personal_website\images"

for filename, url in images.items():
    try:
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code == 200:
            dest = os.path.join(images_dir, filename)
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f"Saved {filename}")
        else:
            print(f"Failed {filename} - Status {r.status_code}")
    except Exception as e:
        print(f"Error {filename}: {e}")
