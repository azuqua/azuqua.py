import json
import requests
import hmac
import datetime
import copy
import hashlib
import urllib.parse as urllib
import os

class Azuqua(object):
    HTTP_OPTIONS = {
        "protocol": "https",
        "host": "api.azuqua.com",
        "port": "443"
    }

    def __init__(self, accessKey, accessSecret):
        self.accessKey = accessKey
        self.accessSecret = accessSecret

        curr_dir = os.path.dirname(__file__)
        with open(os.path.join(curr_dir, "../static/routes.json")) as route_file:
            routes = json.load(route_file)
            for _, group in routes.items():
                for routeName, route in group.items():
                    def outer():
                        method = route["methods"].upper()
                        path = route["path"]
                        urlParams = list(filter(lambda s: s.startswith(":"), path.split("/")))
                        def inner(*args):
                            new_path = path
                            for (idx, param) in enumerate(urlParams):
                                new_path = new_path.replace(param, str(args[idx]))
                            data = {}
                            if method == 'POST' or method == 'PUT' and len(args) > len(urlParams):
                                last_argument = args[len(args) - 1]
                                if isinstance(last_argument, dict):
                                    data = last_argument
                            return self.request(new_path, method, data)
                        return inner
                    setattr(self.__class__, routeName, staticmethod(outer()))

    def account(self):
        return { 
            "accessKey": self.accessKey,
            "accessSecret": self.accessSecret
        }

    def request(self, path, verb, data):
        if (verb == "GET" or verb == "DELETE") and bool(data):
            querystring = urllib.urlencode(data)
            path = path + "?" + querystring
            data = {}

        headers = {
            "Content-Type": "application/json"
        }
        timestamp = datetime.datetime.utcnow().isoformat()
        headers["x-api-accessKey"] = self.accessKey
        headers["x-api-timestamp"] = timestamp
        headers["x-api-hash"] = self.sign_data(self.accessSecret, path, verb, data, timestamp)

        http_options = Azuqua.HTTP_OPTIONS
        url = http_options["protocol"] + "://" + http_options["host"] + ":" + http_options["port"] + path
        if verb == "GET":
            resp = requests.get(url, headers=headers)
            return resp.json() or resp.text
        elif verb == "DELETE":
            resp = requests.delete(url, headers=headers)
            return resp.json() or resp.text
        elif verb == "PUT":
            data = str(json.dumps(data, separators=(',', ':')))
            resp = requests.put(url, data=data, headers=headers)
            return resp.json() or resp.text
        else:
            data = str(json.dumps(data, separators=(',', ':')))
            resp = requests.post(url, data=data, headers=headers)
            return resp.json() or resp.text

    def sign_data(self, secret, path, verb, data, timestamp):
        if not bool(data):
            data = ""
        else:
            data = str(json.dumps(data, separators=(',', ':')))
        meta = str(":".join([verb.lower(), path, timestamp])) + data
        return hmac.new(secret.encode(), meta.encode(), hashlib.sha256).hexdigest()
