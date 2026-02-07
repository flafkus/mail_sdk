# mail_gw

## Description

Thank you to [yxzlwz](https://github.com/yxzlwz) for creating the original mail_gw package!

This is a Python package providing a simple way to create & receive temporary emails. It includes wrappers for both [mail.gw](https://mail.gw/en/) and [mail.tm](https://mail.tm/en/).

## Install

Install from the local directory:

```bash
pip install .
```

Or install in editable mode for development:

```bash
pip install -e .
```

## Usage

```python
# Import from mail_gw
from mail_gw import Account

# Or import from mail_tm
from mail_tm import Account

# Create an account
a = Account(address='test@bluebasketbooks.com.au', password='123456')  # Use the domain listed on the website
a = Account(address='test', password='123456')  # Prefix only, it will randomly choose a domain
a = Account()  # Use both random address and password

# View the address and password
print(a.address, a.password)
# View the account details
print(a.json())

# During initialisation, the account will be registered on mail.gw or mail.tm and the token will be generated automatically.
# If necessary, you can run this code to register and get the token manually.
a.register()
a.get_token()
# Both of the above steps will return the account details.

# Check the email inbox
print(a.get_message(latest=0))
# latest: 0 means the latest email, 1 means the second latest email, and so on.
# If there are no emails, it will raise IndexError.
```

### Using Proxies

You can use proxies in two ways:

```python
# Method 1: Pass proxy directly to Account
from mail_gw import Account

proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

a = Account(proxies=proxies)

# Method 2: Set global proxy for all accounts
from mail_gw import set_proxies, Account

proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

set_proxies(proxies)
a = Account()  # Will use the global proxy
```

Both `mail_gw` and `mail_tm` modules support proxies the same way.
