#!/usr/bin/python

import urllib.request

header = """$TTL 300
@            IN    SOA  localhost. root.localhost.  (
                          1678481389   ; serial - last updated
                          3H  ; refresh
                          1H  ; retry
                          1W  ; expiry
                          1H) ; minimum
                  IN    NS    localhost.

"""
print(header)


url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
with urllib.request.urlopen(url) as f:
    for bytes in f:
        line = bytes.decode("utf-8")
        splitted_line = line.split()
        if (
            len(splitted_line) == 2 
            and splitted_line[0] == "0.0.0.0"
            and splitted_line[1] != "0.0.0.0"
            and "_" not in splitted_line[1]
        ):
            domain = splitted_line[1]
            print(f"{domain} A 0.0.0.0")
