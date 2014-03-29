
import json
import requests
import hmac
import hashlib

class Azuqua(object):

	routes = {
		"invoke": "/api/flo/:id/invoke",
		"list": "/api/account/list"
	}

	http_options = {
		"host": "https://api.azuqua.com",
		"headers": {
			"Content-Type": "application/json",
			"Accept": "*/*"
		}
	}

	def __init__(self, accessKey, accessSecret):
		self.accessKey = accessKey
		self.accessSecret = accessSecret

	def sign_data(self, secret, data):
		return hmac.new(secret, data, hashlib.sha256).hexdigest()

	def make_request(self, path, json):
		body = {
			"accessKey": self.accessKey,
			"data": json,
			"hash": sign_data(self.accessSecret, json)
		}
		resp = requests.post(http_options["host"] + path, data=json.dumps(body), headers=http_options["headers"])
		return resp.json

	def account(self):
		return { 
			"accessKey": self.accessKey,
			"accessSecret": self.accessSecret
			}

	def create_flo(self, name, alias):
		return Azuqua.Flo(self, name, alias)

	def list_flos(self):
		data = json.dumps({})
		resp = make_request(routes["list"], data)
		if resp["error"]:
			return resp["error"]
		else:
			out = []
			for flo in resp["data"]:
				out.append(create_flo(flo["name"], flo["alias"]))
			return out

	class Flo(object):

		def __init__(self, wrapper, name, alias):
			self.name = name
			self.alias = alias
			self.wrapper = wrapper

		def invoke(self, data):
			path = routes["invoke"].replace(":id", self.alias)
			data = json.dumps(data)
			resp = make_request(path, data)
			return resp["error"] if resp["error"] else resp["data"]
			

