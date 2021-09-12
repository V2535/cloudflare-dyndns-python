#!/usr/bin/env python3

# Standard Library
import json
import dns.resolver

# Third Party
import requests

# First Party
from settings import CLOUDFLARE_VARS, DNS_QUERY, SLACK_VARS


def query_existing_ip():
    resolver = dns.resolver.Resolver()
    resolver.nameservers = DNS_QUERY["nameserver"]
    query_host = resolver.resolve(DNS_QUERY["query_host"], "A")
    current_ip = [rdata.address for rdata in query_host][0]
    return current_ip


def query_current_ip():
    url = "https://ifconfig.co/json"
    response = requests.get(url)
    return response.json()["ip"]


def update_slack(current_ip):
    message = {
        "channel": SLACK_VARS["channel"],
        "username": SLACK_VARS["username"],
        "text": f"Your public IP address has been updated to {current_ip}",
    }
    try:
        response = requests.post(
            SLACK_VARS["webhook_url"],
            json=message,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as error:
        return error


def main():
    existing_ip = query_existing_ip()
    current_ip = query_current_ip()
    ret = f"IP address {existing_ip} does not need updating"
    if existing_ip != current_ip:
        try:
            ret = []
            for record in CLOUDFLARE_VARS["RECORDS"]:
                url = (
                    "https://api.cloudflare.com/client/v4/zones/"
                    f"{CLOUDFLARE_VARS['ZONE_ID']}/dns_records/{record['id']}"
                )
                headers = {
                    "X-Auth-Email": CLOUDFLARE_VARS["USER_EMAIL"],
                    "Authorization": f"Bearer {CLOUDFLARE_VARS['API_KEY']}",
                    "Content-Type": "application/json",
                }
                payload = {"type": "A", "name": record["name"], "content": current_ip}
                response = requests.put(url, headers=headers, data=json.dumps(payload)).json()
                output = {
                    "cloudflare_update": response["success"],
                    "hostname": response["result"]["name"],
                    "address": response["result"]["content"],
                }
                ret.append(output)
            if SLACK_VARS["enabled"]:
                slack = update_slack(current_ip)
                ret.append({"slack_update": slack.text})
        except Exception as err:
            ret = f"Something went wrong! {err}"
    print(ret)


if __name__ == "__main__":
    main()
