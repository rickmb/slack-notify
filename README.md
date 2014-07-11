slack-notify
============

Simple little script for pushing notifications to Slack via CLI

```
usage: slack-notify.py [-h] -t TOKEN -d DOMAIN -c CHANNEL message
```

CHANNEL without the "#", couldn't be bothered to make it smarter.

Exampls:

```
./slack-notify.py -t $$$secret$$$$ -d symbid -c test "Just testing"
```
