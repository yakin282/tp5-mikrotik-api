import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
BASE_URL = f"https://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv('DEVICE_USER'), os.getenv('DEVICE_PASSWORD'))

ROUTES = [
    ("10.10.0.0/24", "192.168.100.1"),
    ("10.20.0.0/24", "192.168.100.1"),
    ("172.16.0.0/16", "192.168.56.1"),
]


def get_existing_routes():
    resp = requests.get(f"{BASE_URL}/ip/route", auth=AUTH, verify=False, timeout=5)
    resp.raise_for_status()
    return {(r.get("dst-address"), r.get("gateway")) for r in resp.json()}


def main():
    existing = get_existing_routes()
    for dst, gw in ROUTES:
        if (dst, gw) in existing:
            print(f"[SKIP] {dst} via {gw} existe deja")
            continue
        payload = {"dst-address": dst, "gateway": gw}
        resp = requests.put(f"{BASE_URL}/ip/route", json=payload,
                             auth=AUTH, verify=False, timeout=5)
        resp.raise_for_status()
        print(f"[CREATE] {dst} via {gw}")


if __name__ == "__main__":
    main()
