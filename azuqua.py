
import json
import requests
import hmac
import datetime
import copy
import hashlib
import urllib

class Azuqua(object):

	ROUTES = {
		"list": {
			"path": "/api/account/flos",
			"method": "get"
		},
		"invoke": {
			"path": "/api/flo/:id/invoke",
			"method": "post"
		}
	}

	HTTP_OPTIONS = {
		"host": "https://api.azuqua.com",
		"headers": {
			"Content-Type": "application/json",
			"Accept": "*/*"
		}
	}
 
	def __init__(self, accessKey, accessSecret):
		self.accessKey = accessKey
		self.accessSecret = accessSecret
		self.floCache = None

	def sign_data(self, secret, data, verb, path, timestamp):
		if isinstance(data, dict):
			data = str(json.dumps(data, separators=(',', ':')))
		meta = str(":".join([verb.lower(), path, timestamp]))
		return hmac.new(secret, meta + data, hashlib.sha256).hexdigest()

	def make_request(self, path, verb, data):
		if data is None or len(data) < 1:
			data = ""
		headers = copy.copy(Azuqua.HTTP_OPTIONS["headers"])
		timestamp = datetime.datetime.utcnow().isoformat()
		headers["x-api-accessKey"] = self.accessKey
		headers["x-api-timestamp"] = timestamp
		headers["x-api-hash"] = self.sign_data(self.accessSecret, data, verb, path, timestamp)
		if verb == "get":
			if isinstance(data, dict):
				path += urllib.quote_plus(data)
			resp = requests.get(Azuqua.HTTP_OPTIONS["host"] + path, headers=headers)
			return resp.json() or resp.text
		elif verb == "post":
			resp = requests.post(Azuqua.HTTP_OPTIONS["host"] + path, data=json.dumps(data, separators=(',', ':')), headers=headers)
			return resp.json() or resp.text


	def account(self):
		return { 
			"accessKey": self.accessKey,
			"accessSecret": self.accessSecret
		}

	def create_flo(self, name, alias):
		return Azuqua.Flo(self, name, alias)

	def flos(self, refresh=False):
		if refresh or self.floCache is None:
			resp = self.make_request(Azuqua.ROUTES["list"]["path"], Azuqua.ROUTES["list"]["method"], None)
			if isinstance(resp, dict) and "error" in resp:
				raise Exception(resp["error"] or "Error listing flos")
			else:
				self.floCache = map(lambda curr: self.create_flo(curr["name"], curr["alias"]), resp)
		return self.floCache

	class Flo(object):

		def __init__(self, wrapper, name, alias):
			self.name = name
			self.alias = alias
			self.wrapper = wrapper

		def invoke(self, data):
			path = Azuqua.ROUTES["invoke"]["path"].replace(":id", self.alias)
			resp = self.wrapper.make_request(path, Azuqua.ROUTES["invoke"]["method"], data)
			if isinstance(resp, dict) and "error" in resp:
				raise Exception(resp["error"] or "Error invoking flo")
			else:
				return resp
