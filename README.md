Azuqua Python client
=====================

[PLACEHOLDER_DESC_HERE]

Requirements
============

Python > 3.0

Install
=======

Clone Azuqua.py and run setup tools

```bash
git clone https://github.com/azuqua/azuqua.py/tree/feature/v2API
```

```python
python setup.py install
```

Usage
=====
```python
import Azuqua

ACCESS_KEY = ""
ACCESS_SECRET = ""
azuqua = Azuqua.Azuqua(ACCESS_KEY, ACCESS_SECRET)



print(azuqua.read_all_accounts())


print(azuqua.read_account(account_id))


print(azuqua.delete_account(account_id))

data = {
  "role": "NONE"
}
print(azuqua.update_account_user_permissions(account_id, user_id, data))


print(azuqua.read_connector_version(connector_name, connector_version))


print(azuqua.read_flo(flo_id))

data = {
  "name": "",
  "description": ""
}
print(azuqua.update_flo(flo_id, data))


print(azuqua.delete_flo(flo_id))


print(azuqua.enable_flo(flo_id))


print(azuqua.disable_flo(flo_id))


print(azuqua.read_flo_inputs(flo_id))


print(azuqua.read_flo_accounts(flo_id))


print(azuqua.move_flo_to_folder(flo_id, folder_id))

data = {
  "configs": "",
  "inputs": [],
  "outputs": []
}
print(azuqua.modify_flo(flo_id, data))

data = {
  "folder_id": 0
}
print(azuqua.copy_flo(flo_id, data))

data = {
  "folder_id": 0
}
print(azuqua.copy_flo_to_org(flo_id, org_id, data))


print(azuqua.read_all_folders())

data = {
  "name": "",
  "description": ""
}
print(azuqua.create_folder(data))


print(azuqua.read_folder(folder_id))

data = {
  "name": "",
  "description": ""
}
print(azuqua.update_folder(folder_id, data))


print(azuqua.delete_folder(folder_id))


print(azuqua.read_folder_flos(folder_id))


print(azuqua.read_folder_users(folder_id))

data = {
  "role": "NONE"
}
print(azuqua.update_folder_user_permissions(folder_id, user_id, data))


print(azuqua.read_org())

data = {
  "name": "",
  "display_name": ""
}
print(azuqua.update_org(data))


print(azuqua.read_org_flos())


print(azuqua.read_org_connectors())


print(azuqua.remove_user_from_org(user_id))

data = {
  "role": "MEMBER"
}
print(azuqua.update_org_user_permissions(user_id, data))


print(azuqua.read_user_orgs())
```

LICENSE - "MIT License"
=======================
Copyright (c) 2017 Azuqua

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
