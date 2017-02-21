import os
import json


def get_slack_token():
    return _get_env("SLACK_TOKEN")


def get_lang():
    return _get_env("LANG")


def _get_env(key):
    value = os.environ.get(key, "")
    if not value:
        keys = _get_key_info()
        _key = key.lower()
        if _key in keys:
            value = keys[_key]
    return value
    

def _get_key_info():
    key_file = os.path.join(os.path.dirname(__file__), "../keys.json")
    if os.path.isfile(key_file):
        with open(key_file, encoding="utf-8") as f:
            keys = json.load(f)
    return keys