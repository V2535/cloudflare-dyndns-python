### Cloudflare DynDNS with Python
This allows the updating of multiple DNS records within a given Cloudflare DNS zone. Simply rename `settings_example.py` to `settings.py` and update the variables accordingly.

Currently, only a single DNS zone is supported.

This script can be run as a cron job on a device to frequently check for an updated public IP address.
