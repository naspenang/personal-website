import requests
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

images = {
    "rdms_logo.png": "https://online.library.uitm.edu.my/rdms/Images/rdms_dark.png",
    "iclam_logo.png": "https://online.library.uitm.edu.my/iClam/Images/logo-text.png",
    "era_logo.jpg": "https://online.library.uitm.edu.my/Era/Images/banner.jpg",
    "tourbuilder_logo.png": "https://online.library.uitm.edu.my/TourBuilder/images/logo.png"
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
