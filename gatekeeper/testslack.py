import yaml
import requests
import json
configfile = "../../sneedconfig.yaml"

conf = yaml.safe_load(open(configfile))

print "Using configuration:"
print conf

payload = {
"text":conf['message'],
"channel":conf['channel'],
"icon_emoji":conf['icon_emoji'],
"username": conf['username']
}

def slack(message):
    payload['text'] = message
    r = requests.post(conf['webhookurl'], data = json.dumps(payload))
    print r.text

slack("it works")
