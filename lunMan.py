#!/usr/bin/env python3

import urllib3, time, datetime
import re

PROX = 'https://172.16.1.20:9400'

TICK_URL = "https://api.mybitx.com/api/1/ticker?pair=XBTZAR"
CA_FILE  = "/home/stephanh/Documents/ZscalerIntermediateRootCA(zscalerone.net).crt"

def main():
    ## DSL SSL junk
    #req  = urllib3.Request(TICK_URL)
    #ssl = urllib3.HTTPSHandler()
    #cxt = ssl.create_default_context(cafile=CA_FILE)

    #https = urllib3.ProxyManager(
    #        PROX,
    #        cert_reqs='CERT_REQUIRED',
    #        ca_certs=CA_FILE)
    #https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=CA_FILE)

    d_re = re.compile('.*\"timestamp\":(\d*).*\"bid\":\"(\d*.\d*)\".*\"ask\":\"(\d*.\d*)\".*')
    https = urllib3.PoolManager()

    for i in range(5):
        resp = https.request('GET', TICK_URL, timeout=5.0)

        #resp = urllib3.urlopen(req, context=cxt)
        data = d_re.match(resp.data.decode("utf-8","strict"))
        if data:
            timestamp = datetime.datetime.fromtimestamp(int(data.group(1))/1000)
            bid = data.group(2)
            ask = data.group(3)

            print(timestamp)
            print("BID: R" + bid)
            print("ASK: R" + ask)
        else:
            print("Failed to connect")
        time.sleep(2)


if __name__ == "__main__":
    main()
