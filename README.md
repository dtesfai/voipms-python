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

- Python 2.7+ or 3.4+

## Usage

The library needs to be configured with your account's email and API password, the latter of which can be created [here](https://voip.ms/m/api.php). Set the variables `voipms.email` and `voipms.apikey` to their respective values:

```python
import voipms

voipms.email = "test@email.com"
voipms.api_key = "01N0sWTdiutWTHNF"

# get current account balance
voipms.general.get_balance()

# remove did from account
voipms.dids.cancel_dids(did="5551234567")
```
