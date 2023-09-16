# oppe-for-python
[![codecov](https://codecov.io/gh/kilobyteno/oppe-for-python/graph/badge.svg?token=JKLDG13D1W)](https://codecov.io/gh/kilobyteno/oppe-for-python)
[![PyPI version](https://badge.fury.io/py/oppe.svg)](https://badge.fury.io/py/oppe)
[![Downloads](https://pepy.tech/badge/oppe)](https://pepy.tech/project/oppe)
[![License](https://img.shields.io/github/license/kilobyteno/oppe-for-python)](LICENSE)

An API wrapper for [Oppe](https://oppe.app) written in Python.


## Installation

```bash
pip install oppe
```

## Usage

### Sending an event

```python
from oppe import Oppe
from oppe.exceptions import EventRequestError

oppe = Oppe(api_token='insert-api-token-here', project_id="uuid-of-project")

try:
    oppe.event(
        channel_id="uuid-of-channel",
        title="user-registered",
        description="A new user has registered.",
        emoji="👋",
        data={
            "user_id": 123,
        },
    )
except EventRequestError as e:
    # Handle error
    print(e)
```
