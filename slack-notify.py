#!/usr/bin/env python
import argparse
import json
import urllib

class SlackWebHook:

    def __init__(self, domain, token):
        self.token = token
        self.domain = domain

    def _request(self, payload):
        url = "https://%s.slack.com/services/hooks/incoming-webhook?token=%s" % (self.domain, self.token)
        data = urllib.urlencode({"payload": json.dumps(payload)})
        response = urllib.urlopen(url, data).read()
        if response == "ok":
            return True
        else:
            print "Error: %s" % response
            return False

    def notify(self, channel, text, **params):
        channel = "#" + channel
        params.update({
            'channel': channel,
            'text': text,
        })
        return self._request(params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', dest='token', required=True)
    parser.add_argument('-d', '--domain', dest='domain', required=True)
    parser.add_argument('-c', '--channel', dest='channel', required=True)
    parser.add_argument('message')

    args = parser.parse_args()
    slack = SlackWebHook(args.domain, args.token)

    if slack.notify(args.channel, args.message):
        exit(0)
    else:
        exit(1)








