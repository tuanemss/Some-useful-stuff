import os
import requests

BASE_URL = "http://cydia.vn"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "debs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

packages_path = os.path.join(os.path.dirname(__file__), "Packages")

with open(packages_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if line.startswith("Filename: "):
            file_path = line.strip().split("Filename: ")[1]
            full_path = os.path.join(OUTPUT_DIR, file_path)
            dir_path = os.path.dirname(full_path)

            os.makedirs(dir_path, exist_ok=True)

            url = f"{BASE_URL}/{file_path}"
            print(f"Downloading: {file_path}")

            try:
                response = requests.get(url, timeout=20)
                if response.status_code == 200:
                    with open(full_path, "wb") as deb_file:
                        deb_file.write(response.content)
                else:
                    print(f"Failed ({response.status_code}): {url}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")

