### Cloudflare Dynamic DNS updater with Slack integration
This allows the updating of multiple DNS records within a given Cloudflare DNS zone. Simply rename `settings_example.py` to `settings.py` and update the variables accordingly.

Currently, only a single DNS zone is supported.

This script can be run as a cron job on a device to frequently check for an updated public IP address.

You can configure this script to post to a Slack channel by changing `SLACK_VARS["enabled"]` to `True` and configuring the appropriate values.

The script will only update Cloudflare, and post to Slack if your current IP differs from that of another hostname. Therefore, it is a good idea to enter the FQDN of a hostname you are updating with Cloudflare in `DNS_QUERY["query_host"]`. The default nameservers are 8.8.8.8 and 8.8.4.4.

![Slack example](https://raw.githubusercontent.com/dsgnr/cloudflare-dyndns-python/master/assets/example.png)


### Example output

~~~ shell
./cloudflare_dyndns.py
[{'success': True, 'name': 'dns1.example.com', 'content': '1.1.1.1'}
{'success': True, 'name': 'dns2.example.com', 'content': '1.1.1.1'}
{'success': True, 'name': 'dns3.example.com', 'content': '1.1.1.1'}
{'success': True, 'name': 'dns4.example.com', 'content': '1.1.1.1'},
{'slack_update': 'ok'}]
~~~

#### Considerations for Python 3 environments lower than Python 3.6

This script uses f-strings which were introduced in Python 3.6. If you are using a Python 3 version that does not support f-strings, you can either modify the script to use a supported method, or install a pip <https://pypi.org/project/future-fstrings/>. The script can be run with only adding `# -*- coding: future_fstrings -*-` to the top of the file.
