# voipms-python

A python-based API wrapper for [voip.ms](https://voip.ms/).

## Installation

You can install this package from PyPi using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python. Once pip is installed, run

```sh
pip install --upgrade voipms-python
```

You can also install from source with:

```sh
python setup.py install
```

### Requirements

- Python 3.4+

## Usage

The library needs to be configured with your account's email and API password, the latter of which can be created [here](https://voip.ms/m/api.php). Once that's been done, create a Client object as shown below:

```python
from voipms.api import Client

email = "test@email.com"
api_password = "01N0sWTdiutWTHNF"

client = Client(email, api_password)

# get current account balance
balance = client.balance.fetch()
```
