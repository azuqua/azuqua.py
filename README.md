azuqua.py
=========

Python library for invoking Flõs on Azuqua.

Usage example:

```
import os
import azuqua

# Accessing the API via access key and access secret.
# In this case, we're grabbing the key and secret from the ENV variables.
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

azuquaObject = azuqua.Azuqua(ACCESS_KEY, ACCESS_SECRET)
for flo in azuquaObject.flos():
	flo.invoke(data)
	flo.read()
	flo.enable()
	flo.disable()

# Accessing the API via a username and password
EMAIL = os.getenv('AZUQUA_EMAIL')
PASSWORD = os.getenv('AZUQUA_PASSWORD')

azuquaObject = azuqua.Azuqua()

# login returns a list of orgs associated with the username
orgs = azuquaObject.login(EMAIL, PASSWORD)
for org in orgs:
	for flo in org.flos():
		flo.invoke(data)
		flo.read()
		flo.enable()
		flo.disable()
```
