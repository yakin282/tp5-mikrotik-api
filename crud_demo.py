import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
BASE_URL = f"https://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv('DEVICE_USER'), os.getenv('DEVICE_PASSWORD'))
ADDRESS = "192.168.20.1/24"


def show(title, resp):
    print(f"\n=== {title} ({resp.status_code}) ===")
    try:
        print(resp.json())
    except ValueError:
        print("(pas de contenu)")


# GET
resp = requests.get(f"{BASE_URL}/ip/address", auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
show("GET /ip/address", resp)

# POST
payload = {"address": ADDRESS, "interface": "ether2"}
resp = requests.put(f"{BASE_URL}/ip/address", json=payload, auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
show("POST /ip/address", resp)

# GET filtré pour retrouver le .id
resp = requests.get(f"{BASE_URL}/ip/address", params={"address": ADDRESS},
                    auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
show("GET filtré", resp)
addr_id = resp.json()[0][".id"]

# PATCH
resp = requests.patch(f"{BASE_URL}/ip/address/{addr_id}", json={"comment": "TP5 - modifie via API"},
                      auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
show("PATCH", resp)

import time; print("\nPrends ta capture MAINTENANT (60 secondes)..."); time.sleep(60)

# DELETE
resp = requests.delete(f"{BASE_URL}/ip/address/{addr_id}", auth=AUTH, verify=False, timeout=5)
resp.raise_for_status()
print(f"\n=== DELETE ({resp.status_code}) === adresse {ADDRESS} supprimee")
