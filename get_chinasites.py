#!/usr/bin/env python3

from urllib.request import urlopen

dns='114.114.114.114;119.29.29.29'
conf_url = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf'
dnsmasq_conf = urlopen(conf_url).read().decode('utf8')
bind9_zone=[]
TEMPLATE = ('zone \"{DOMAIN}\" {{type forward;forwarders {{{DNS};}};}};\n')
for line in dnsmasq_conf.split('\n'):
        entry = line.split('/')
        if len(entry) != 3:
            continue
        bind9_zone.append(TEMPLATE.format(DOMAIN=entry[1], DNS=dns))
        pass
file=open('/etc/bind/named.conf.chinasites','w')
for l in bind9_zone:
	file.write(l)
	pass
file.close()