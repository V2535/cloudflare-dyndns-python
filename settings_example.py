# Use something like the following to obtain the record IDs from a zone in Cloudflare:
#curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
#     -H "X-Auth-Email: email@example.com" \
#     -H "X-Auth-Key: api_key" \
#     -H "Content-Type: application/json"

DNS_QUERY ={
    "query_host": "example.domain.com",
    "nameserver": ["8.8.8.8", "8.8.4.4"]
}

SLACK_VARS = {
    "enabled": False,
    "webhook_url": "https://hooks.slack.com/services/<foo>",
    "username": "IP Updater",
    "channel": "#channel_name",
}

CLOUDFLARE_VARS = {
    "API_KEY": "cloudflare_api_key",
    "USER_EMAIL": "cloudflare_email_address",
    "ZONE_ID": "dns_zone_id",
    "RECORDS": [
        {"name": "test.example.com", "id": "record_id"},
        {"name": "test1.example.com", "id": "record_id"},
    ],
}
