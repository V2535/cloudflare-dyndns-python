#!/usr/bin/env python3

# Standard Library
import json

# Third Party
import requests

# First Party
from settings import CLOUDFLARE_VARS


def get_ip():
    url = "https://ifconfig.co/json"
    response = requests.get(url)
    return response.json()["ip"]


def main():
    public_ip = get_ip()
    for record in CLOUDFLARE_VARS["RECORDS"]:
        url = f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_VARS['ZONE_ID']}/dns_records/{record['id']}"
        headers = {
            "X-Auth-Email": CLOUDFLARE_VARS["USER_EMAIL"],
            "X-Auth-Key": CLOUDFLARE_VARS["API_KEY"],
            "Content-Type": "application/json",
        }

        payload = {"type": "A", "name": record["name"], "content": public_ip}
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        ret = response.json()
        output = {
            "success": ret["success"],
            "name": ret["result"]["name"],
            "content": ret["result"]["content"],
        }
        print(output)


if __name__ == "__main__":
    main()
