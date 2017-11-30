#!/usr/bin/env python3

import urllib3

PROX = 'https://172.16.1.20:9400'

TICK_URL = "https://api.mybitx.com/api/1/ticker?pair=XBTZAR"
CA_FILE  = "/home/stephanh/Documents/ZscalerIntermediateRootCA(zscalerone.net).crt"

def main():
    #req  = urllib3.Request(TICK_URL)
    #ssl = urllib3.HTTPSHandler()
    #cxt = ssl.create_default_context(cafile=CA_FILE)

    #https = urllib3.ProxyManager(
    #        PROX,
    #        cert_reqs='CERT_REQUIRED',
    #        ca_certs=CA_FILE)
    #https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=CA_FILE)
    https = urllib3.PoolManager()
    r = https.request('GET', 'https://www.google.com', timeout=5.0, verify=False)

    #resp = urllib3.urlopen(req, context=cxt)
    #tickerdat = resp.read()
    print(r)

if __name__ == "__main__":
    main()
