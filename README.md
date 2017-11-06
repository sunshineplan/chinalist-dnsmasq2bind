# chinalist-dnsmasq2bind
Convert dnsmasq-china-list configuration to bind9 version.

Configure named.conf, add a line at the end of it:
```
include "/etc/bind/named.conf.chinasites";
```

You can replace dns value if you need.

## Refer：
https://oing9179.github.io/blog/2016/09/Clean-DNS-Server-Setup-Using-bind9-and-dnscrypt-proxy/
https://github.com/felixonmars/dnsmasq-china-list
